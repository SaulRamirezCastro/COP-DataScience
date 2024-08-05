terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}


resource "aws_iam_role" "lambda_role_cop_metadata" {
  name = "Lambda_role_Cop_metadata"
  description = "Lambda role to write metadata in dynamodb"
  assume_role_policy = ""
}

resource "aws_iam_policy" "lambda_policy_cop_metadata" {
  policy = ""
  path = "/"
  name = "lambda_policy_cop_metadata"
  description = "Aww policy for lambda to write metadata in dynano "
}

resource "aws_iam_role_policy_attachment" "attach_iam_policy_cop_metadata" {
   role = aws_iam_role.lambda_role_cop_metadata.name
  policy_arn = aws_iam_policy.lambda_policy_cop_metadata.arn
}

data "archive_file" "zip_python_code" {
  type        = "zip"
  source_dir = "${path.root}./metadata/"
  output_path = "${path.module}/metadata/lambda_athena.zip"
}

resource "aws_lambda_function" "lambda_COP_metadata" {
  function_name = "lambda_cop_metadata"
  role          = aws_iam_role.lambda_role_cop_metadata.arn
  filename = "${path.module}/metadata/lambda_athena.zip"
  handler = "lambda_function.lambda_handler"
  runtime = "python3.8"
  timeout = 300
  layers = ["arn:aws:lambda:us-east-1:553264372403:layer:layer:1"]
  depends_on = [aws_iam_role_policy_attachment.attach_iam_policy_cop_metadata]
}

resource "aws_lambda_event_source_mapping" "event_cop_metadata" {
  event_source_arn = aws_sqs_queue.sqs_cop_metadata.arn
  function_name    = aws_lambda_function.lambda_COP_metadata.function_name
  batch_size = 1

}

resource "aws_sqs_queue" "sqs_cop_metadata" {
  name = "Sqs_Cop_metadata"
  delay_seconds = 1
  visibility_timeout_seconds = 30
  max_message_size = 2048

}