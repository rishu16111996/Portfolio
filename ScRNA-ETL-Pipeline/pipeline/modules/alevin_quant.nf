process ALEVIN_QUANT {
    tag "${sample_id}"
    publishDir "${params.outdir}/quant/${sample_id}", mode: 'copy'

    input:
    tuple val(sample_id), path(r1), path(r2)

    output:
    tuple val(sample_id), path("alevin_output"), path("alevin_meta.json")

    script:
    // Alevin USA mode example; adjust chemistery flags
    """
    if [ -z "${params.salmon_index}" ]; then
        echo "ERROR: --salmon_index is required" >&2
        exit 1
    fi

    mkdir -p alevin_out

    # Note: this is generic salmon alevin call
    # --chromiumV3 or use alevin-fry 
    salmon alevin \\
        -l ${params.libtype} \\
        -i ${params.salmon_index} \\
        -1 ${r1} -2 ${r2} \\
        -p ${task.cpus} \\
        --tgMap ${params.salmon_index}/t2g.tsv \\
        -o alevin_out 

    python - << 'PY'
    import json, os, time

    meta = {
        "sample_id": "${sample_id}",
        "run_id": "${params.run_id}",
        "timestamp": int(time.time()),
        "tool": "salmon_alevin",
        "output_dir": "alevin_out",
    }

    with open("alevin_meta.json", "w") as f:
        json.dump(meta, f, indent=2)

    PY
    """
}