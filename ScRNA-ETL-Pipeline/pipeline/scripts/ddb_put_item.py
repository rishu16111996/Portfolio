import os
import json
import time
import argparse
from typing import Any, Dict

import boto3


def load_json(path: str) -> Dict[str, Any]:
    with open(path, "r") as f:
        return json.load(f)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--table", required=True, help="DynamoDB table name")
    p.add_argument("--region", default=os.getenv("AWS_REGION", "us-east-1"))
    p.add_argument("--run-id", required=True)
    p.add_argument("--sample-id", required=True)
    p.add_argument("--status", default="COMPLETED")
    p.add_argument("--qc-json", required=True, help="Path to qc_metrics.json")
    p.add_argument("--artifacts-json", required=False, help="Path to artifacts.json (optional)")
    p.add_argument("--out-bucket", required=False, help="S3 bucket for output (optional)")
    p.add_argument("--out-prefix", required=False, help="S3 prefix for output (optional), e.g. results/")
    args = p.parse_args()

    qc = load_json(args.qc_json)

    artifacts: Dict[str, Any] = {}
    if args.artifacts_json and os.path.exists(args.artifacts_json):
        artifacts = load_json(args.artifacts_json)

    item: Dict[str, Any] = {
        "run_id": args.run_id,                 # partition key
        "sample_id": args.sample_id,
        "status": args.status,
        "timestamp": int(time.time()),
        # QC fields (flattened)
        "cells": int(qc.get("cells", 0)),
        "genes": int(qc.get("genes", 0)),
        "median_counts_per_cell": float(qc.get("median_counts_per_cell", 0.0)),
        "median_genes_per_cell": float(qc.get("median_genes_per_cell", 0.0)),
        # optional structure
        "qc": qc,
        "artifacts": artifacts,
    }

    if args.out_bucket:
        item["output_bucket"] = args.out_bucket
    if args.out_prefix:
        item["output_prefix"] = args.out_prefix

    ddb = boto3.resource("dynamodb", region_name=args.region)
    table = ddb.Table(args.table)
    table.put_item(Item=item)

    print(json.dumps({"ok": True, "run_id": args.run_id, "sample_id": args.sample_id}, indent=2))


if __name__ == "__main__":
    main()
