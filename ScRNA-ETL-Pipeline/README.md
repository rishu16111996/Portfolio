# scETL: End-to-End Single-Cell RNA-Seq Data Engineering Platform

## Overview

scETL is a production-style, end-to-end data engineering platform for processing and managing single-cell RNA-seq data.
The project demonstrates how raw sequencing data (FASTQ files) can be ingested, processed, tracked, stored, and visualized using modern workflow orchestration, cloud infrastructure, APIs, and frontend tools.

This repository is intentionally designed to mirror real-world infrastructure and workflow patterns used in biotech and computational biology teams. The focus is on data pipelines, reproducibility, scalability, and engineering rigor, rather than biological novelty.

The platform covers the full lifecycle:

- Raw data ingestion
- Scalable workflow orchestration
- Containerized compute
- Cloud storage and metadata tracking
- APIs for downstream access
- A lightweight frontend for monitoring and visualization


## High-Level Architecture

1. Input
   - Public single-cell RNA-seq FASTQ files (10x Genomics or SRA)
   - Stored locally or in Amazon S3

2. Processing Layer
   - Nextflow DSL2 workflow
   - Dockerized bioinformatics tools
   - Salmon Alevin for quantification
   - Scanpy for downstream QC and embeddings

3. Storage
   - Amazon S3 for raw and processed data
   - DynamoDB for metadata, run tracking, and QC summaries

4. Service Layer
   - FastAPI backend to expose pipeline metadata and artifacts
   - Presigned S3 URLs for secure artifact access

5. Frontend
   - React dashboard for viewing pipeline runs and QC metrics

6. Infrastructure
   - Terraform for infrastructure as code
   - AWS Batch support for scalable execution
   - GitHub Actions for CI and validation


## Technology Stack

Workflow Orchestration
- Nextflow (DSL2)

Compute and Containers
- Docker
- AWS Batch

Bioinformatics
- Salmon Alevin
- FastQC
- MultiQC
- Scanpy

Backend
- FastAPI
- Python
- boto3

Frontend
- React
- Vite

Cloud Infrastructure
- AWS S3
- AWS DynamoDB
- IAM
- Terraform

CI/CD
- GitHub Actions


## Repository Structure

project-root/
├── aws/                    Terraform infrastructure
├── pipeline/               Nextflow pipeline and Docker image
│   ├── main.nf
│   ├── nextflow.config
│   ├── Dockerfile
│   └── modules/
├── api/                    FastAPI backend
├── frontend/               React dashboard
├── .github/workflows/      CI/CD workflows
└── README.md


## Example Dataset Download

This project uses a public 10x Genomics single-cell RNA-seq dataset.

Dataset
- 10k Peripheral Blood Mononuclear Cells (PBMC)
- 10x Chromium 3’ v3.1

Direct FASTQ Download Link
https://cf.10xgenomics.com/samples/cell-exp/3.1.0/10k_pbmcs_3p_nextgem_3.1.0/10k_pbmcs_3p_nextgem_3.1.0_fastqs.tar


Download and extract:

wget https://cf.10xgenomics.com/samples/cell-exp/3.1.0/10k_pbmcs_3p_nextgem_3.1.0/10k_pbmcs_3p_nextgem_3.1.0_fastqs.tar
tar -xvf 10k_pbmcs_3p_nextgem_3.1.0_fastqs.tar


## Pipeline Overview

For each sample, the pipeline performs:

1. FASTQ quality control using FastQC
2. Aggregated QC reporting using MultiQC
3. Single-cell quantification using Salmon Alevin
4. Post-processing and QC using Scanpy
   - Cell and gene counts
   - Median counts per cell
   - UMAP embeddings
5. Metadata and QC metrics logging to DynamoDB

Each step is modular, containerized, and restartable.


## Running the Pipeline Locally

Build the pipeline Docker image:

cd pipeline
docker build -t local/scetl:latest .


Build a Salmon index:

salmon index -t transcripts.fa -i salmon_index


Run the pipeline:

nextflow run main.nf -profile local \
  --reads "/path/to/fastqs/*_{R1,R2}.fastq.gz" \
  --salmon_index "/path/to/salmon_index" \
  --outdir results \
  --ddb_table scetl_runs \
  --aws_region us-east-1


Outputs include:
- MultiQC report
- QC metrics JSON
- UMAP coordinates CSV
- DynamoDB run record


## Metadata Tracking

Each pipeline run logs a structured record to DynamoDB, including:

- run_id
- sample_id
- status
- timestamp
- QC metrics
- artifact locations

This enables downstream querying, dashboards, and auditability.


## FastAPI Backend

The backend provides:
- Run listing and metadata access
- Individual run lookup
- Presigned S3 URLs for artifacts


Run locally:

cd api
docker build -t scetl-api:local .
docker run -p 8000:8000 \
  -e AWS_REGION=us-east-1 \
  -e DDB_TABLE=scetl_runs \
  -e OUTPUT_BUCKET=your-bucket-name \
  scetl-api:local


## React Dashboard

The frontend displays:
- Pipeline runs
- Sample-level QC metrics
- Execution status


Run locally:

cd frontend
npm install
npm run dev

Set:
VITE_API_BASE=http://localhost:8000


## Infrastructure Provisioning

Terraform provisions:
- S3 bucket for data
- DynamoDB table for metadata
- IAM policies for pipeline and API access


cd aws
terraform init
terraform apply -var="bucket_name=your-unique-bucket"


## CI/CD

GitHub Actions performs:
- Nextflow syntax validation
- Docker image build checks
- Terraform formatting and validation

This ensures reproducibility and prevents configuration drift.


## Why This Project Exists

This project was built to demonstrate how to design and operate real data pipelines, integrate scientific workflows with modern infrastructure, manage metadata and observability in research systems, and build interfaces that scientists and downstream teams can use.

It reflects the type of systems I enjoy building and maintaining in collaborative research environments.


## Author

Rishabh Narula
Computational Biologist and Data Engineer

GitHub: https://github.com/rishu16111996
LinkedIn: https://www.linkedin.com/in/rishabh-narula-7a6a3b192
