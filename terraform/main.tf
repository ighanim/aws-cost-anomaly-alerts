provider "aws" {
  region = "us-east-1"
}

data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${path.module}/../src"
  output_path = "${path.module}/../lambda-package-v1.0.0.zip"
}

data "aws_region" "current" {}
variable "app_config_layer_arn" {
  type = map(string)
  default = {
    "us-east-1" = "arn:aws:lambda:us-east-1:027255383542:layer:AWS-AppConfig-Extension:44"
    # Add mappings for other regions if needed
  }
}





