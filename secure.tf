# Safer Checkov/Terraform comparison fixture. Do not apply without review.
resource "aws_s3_bucket" "private_test_bucket" {
  bucket = "sycur-security-fixture-private-do-not-deploy"
}

resource "aws_s3_bucket_public_access_block" "private_test_bucket" {
  bucket                  = aws_s3_bucket.private_test_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

