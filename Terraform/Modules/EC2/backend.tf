terraform {
  backend "s3" {
    bucket         = "your-bucket-name"
    key            = "ec2/terraform.tfstate"
    region         = "us-west-2"  # Specify the appropriate AWS region
    dynamodb_table = "terraform-lock"  # Optional: Enable DynamoDB locking
    encrypt        = true  # Optional: Encrypt the state file
  }
}