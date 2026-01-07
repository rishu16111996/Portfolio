#!/usr/bin/env nextflow
nextflow.enable.dsl = 2

include { FATSQC } from  './modules/qc_fastqc'
include { MULTIQC } from './modules/qc_multiqc'
include { ALEVIN_QUANT} from './modules/alevin_quant'
include { SCANPY_POST} from '.modules/postprocess_scanpy'
include { LOG_TO_DYNAMODB } from './modules/log_to_dynamodb'


workflow{

    if (!params.run_id) {
        params.run_id = "${workflow.projectDir.getName()}-${workflow.launchId}"
    }

    Channel
        .fromPath(params.reads ?: '')
        .ifEmpty { params.sample_sheet ? Channel.empty() : error("Provide --reads or --sample_sheet") }
        .set { reads_glob_ch }

    // Option A: sample_sheet CSV 
    Channel
        .fromPath(params.sample_sheet ?: '')
        .ifEmpty { Channel.empty() }
        .splitCsv(header: true)
        .map { row -> tuple(row.sample_id as String, file(row.r1), file(row.r2)) }
        .set { sample_ch }

    // Option B: infer sample_id from filename pairs 
    // expects: SAMPLE_R1.fastq.gz and SAMPLE_R2.fastq.gz
    reads_glob_ch
        .map { f -> tuple(f.baseName.replaceAll(/_R[12].*$/, ''), f) }
        .groupTuple()
        .map { sample_id, files ->
            def r1 = files.find { it.name.contains('_R1') }
            def r2 = files.find { it.name.contains('_R2') }
            if(!r1 || !r2) error("Could not find R1/R2 for sample ${sample_id} in ${files}") 
            tuple(sample_id as String, r1, r2)   
        }
        .set { inferred_pairs_ch }

    def pairs_ch = params.sample_sheet ? sheet_ch : inferred_pairs_ch

    // QC per sample
    fastqc_out = FASTQC(pairs_ch)
    multiqc_out = MULTIQC(fastqc_out.collect())

    // QUANT (Alevin)
    quant_out = ALEVIN_QUANT(pairs_ch)

    // PostProcessing (scanpy): generate basic QC + UMAP json/CSV
    scanpy_out = SCANPY_POST(quant_out) 

    // scanpy_out emits: tuple(sample_id), qc_metrics.json, umap_points.csv
    ddb_out = LOG_TO_DYNAMODB(scanpy_out)
    ddb_out.view { "DDB_LOGGED: ${it}" }

    // Publish
    multiqc_out.view { "MULTIQC: ${it}" }
    scanpy_out.view { "SCANPY: ${it}" }
}