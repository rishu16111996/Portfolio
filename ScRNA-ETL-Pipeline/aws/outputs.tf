output "bucket_name" {
    value = aws_s3_bucket.data.bucket
}

output "ddb_table_name" {
    value = aws_dynamodb_table.runs.name
}

output "app_policy_arn" {
    value = aws_iam_pollicy.app_policy.arn
}