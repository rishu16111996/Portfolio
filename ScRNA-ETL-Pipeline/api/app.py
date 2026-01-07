import os
import json
from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException
import boto3


AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
DDB_TABLE = os.getenv("DDB_TABLE", "scetl_runs")
OUTPUT_BUCKET = os.getenv("OUTPUT_BUCKET")

ddb = boto3.resource("dynamodb", region_name=AWS_REGION)
s3 = boto3.client("s3", region_name=AWS_REGION)

app = FastAPI(title = "scetl API")


def table():
    return ddb.Table(DDB_TABLE)


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/runs")
def list_runs(limit: int = 50) -> Dict[str, Any]:
    resp = table().scan(Limit=limit)
    items = resp.get("Items", [])
    items.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
    return {"items": items}


@app.get("/run/{run_id}")
def get_run(run_id: str) -> Dict[str, Any]:
    resp = table().get_item(Key={"run_id": run_id})
    item = resp.get("Item")
    if not item:
        raise HTTPException(status_code=404, detail="run_id not found")
    return item


@app.get("/runs/{run_id}/artifact")
def get_artifact(run_id: str, key: str) -> Dict[str, str]:
    """
    returns a presigned URL for an artifact stored in S3.
    Example key: results/analysis/SAMPLE/umap_points.csv
    """
    if not OUTPUT_BUCKET:
        raise HTTPException(status_code = 500, detail="OUTPUT_BUCKET env not set")
    
    if ".." in key or key.startswith("/"):
        raise HTTPException(status_code=400, detail="INVALID KEY")
    
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": OUTPUT_BUCKET, "Key": key},
        ExpiresIn=3600,
    )
    return {"url": url}