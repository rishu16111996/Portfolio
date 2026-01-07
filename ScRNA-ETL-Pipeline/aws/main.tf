terraform {
    required_version = ">= 1.6.0"
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = ">= 5.0"
        }
    }
}

provider "aws" {
    region = var.region
}

resource "aws_s3_bucket" "data" {
    bucket = var.bucket_name
}

resource "aws_s3_bucket_versioning" "data" {
    bucket = aws_s3_bucket.data.id
    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_dynamodb_table" "runs" {
    name = var.ddb_table_name
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "run_id"

    attribute {
        name = "run_id"
        type = "S"
    }
}

data "aws_iam_policy_document" "app_policy" {
    statement {
        actions = [
            "s3:GetObject",
            "s3:PutObject",
            "s3:ListBucket"
        ]
        resource = [
            aws_s3_bucket.data.arn, 
            "${aws_s3_bucket.data.arn}/*"
        ]
    }

    statement{
        actions = [
            "dynamodb:PutItem",
            "dynamodb:GetItem",
            "dynamodb:Scan",
            "dynamodb:UpdateItem"
        ]
        resource = [
            aws_dynamodb_table.runs.arn
        ]
    }
}

resource "aws_iam_policy" "app_policy" {
    name = "${var.project}-app-policy"
    policy = data.aws_iam_policy_document.app_policy.json
}