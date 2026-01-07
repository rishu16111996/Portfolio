variable "prject" {
    type = string
    default = "scetl"
}

variable "region" {
    type = string
    default = "us-east-1"
}

variable "bucket_name" {
    type = string
}

variable "ddb_table_name" {
    type = string
    default = "scelt_runs"
}