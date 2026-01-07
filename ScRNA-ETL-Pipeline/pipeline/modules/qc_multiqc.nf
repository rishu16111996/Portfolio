process MULTIQC {
    publishDir "${params.outdir}/qc/multiqc", mode: 'copy'

    input:
    path(fastqc_artifacts)

    output:
    path("multiqc_report.html")

    script:
    """
    multiqc .
    """
}