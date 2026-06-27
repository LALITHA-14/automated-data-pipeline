variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "s3_bucket_name" {
  description = "S3 Bucket Name"
  type        = string
  default     = "etl-pipeline-bucket"
}