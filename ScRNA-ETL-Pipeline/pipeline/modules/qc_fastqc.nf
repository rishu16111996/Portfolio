process FASTQC {
    tag "${sample_id}"
    publishDir "${params.outdir}/qc/fastqc", mode: 'copy'

    input: 
    tuple val(sample_id), path(r1), path(r2)

    output:
    tyuple val(sample_id), path("*_fastqc.zip"), path("*_fastqc.html")

    script:
    """
    fastqc -t 2 ${r1} ${r2}
    """

}