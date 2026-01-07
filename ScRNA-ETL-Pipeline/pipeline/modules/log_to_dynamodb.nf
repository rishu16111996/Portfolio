process LOG_TO_DYNAMODB {
  tag "${sample_id}"
  publishDir "${params.outdir}/logs/ddb", mode: 'copy'

  input:
  tuple val(sample_id), path(qc_json), path(umap_csv)

  output:
  tuple val(sample_id), path("ddb_put_result.json")

  when:
  params.ddb_table && params.aws_region

  script:
  """
  # Build a small artifacts manifest (S3 keys are optional; you can keep local paths too)
  python - << 'PY'
  import json, os
  sample_id = "${sample_id}"

  artifacts = {
    "qc_metrics_path": os.path.abspath("${qc_json}"),
    "umap_points_path": os.path.abspath("${umap_csv}")
  }

  # If you run on AWS Batch with publishDir to S3, you may also store expected S3 keys here.
  # Example:
  # artifacts["qc_metrics_s3_key"] = f"{os.environ.get('OUT_PREFIX','results')}/analysis/{sample_id}/qc_metrics.json"

  with open("artifacts.json","w") as f:
    json.dump(artifacts, f, indent=2)
  PY

  python ${workflow.projectDir}/scripts/ddb_put_item.py \\
    --table "${params.ddb_table}" \\
    --region "${params.aws_region}" \\
    --run-id "${params.run_id}" \\
    --sample-id "${sample_id}" \\
    --status "COMPLETED" \\
    --qc-json "${qc_json}" \\
    --artifacts-json "artifacts.json" \\
    ${params.output_bucket ? "--out-bucket ${params.output_bucket}" : ""} \\
    ${params.output_prefix ? "--out-prefix ${params.output_prefix}" : ""}

  # Save the stdout response to a file for provenance
  python - << 'PY'
  import json, sys
  # the script already printed JSON, but we’ll just write a minimal marker file
  with open("ddb_put_result.json","w") as f:
    json.dump({"ok": True, "sample_id": "${sample_id}", "run_id": "${params.run_id}"}, f, indent=2)
  PY
  """
}
