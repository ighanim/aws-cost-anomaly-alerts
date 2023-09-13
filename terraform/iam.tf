resource "aws_iam_policy" "ReadAppConfigLambdaPolicy" {
  name        = "ReadAppConfigLambdaPolicy"
  description = "IAM policy to read AppConfig configurations"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "appconfig:GetConfiguration"
      Resource = "*"
    }]
  })

  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_iam_policy" "DescribeAccountNameLambdaPolicy" {
  name = "DescribeAccountNameLambdaPolicy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "organizations:DescribeAccount"
      Resource = "arn:aws:organizations::*:account/o-*/*"
    }]
  })

  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_iam_policy" "GetSecretValueLambdaPolicy" {
  name = "GetSecretValueLambdaPolicy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "secretsmanager:GetSecretValue"
      Resource = "*"
    }]
  })

  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_iam_role" "CostAnomalyAlertsLambdaRole" {
  name = "CostAnomalyAlertsLambdaRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })

  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_iam_policy_attachment" "ReadAppConfigLambdaPolicyAttachment" {
  name       = "ReadAppConfigLambdaPolicyAttachment"
  policy_arn = aws_iam_policy.ReadAppConfigLambdaPolicy.arn
  roles      = [aws_iam_role.CostAnomalyAlertsLambdaRole.name]
}

resource "aws_iam_policy_attachment" "DescribeAccountNameLambdaPolicyAttachment" {
  name       = "DescribeAccountNameLambdaPolicyAttachment"
  policy_arn = aws_iam_policy.DescribeAccountNameLambdaPolicy.arn
  roles      = [aws_iam_role.CostAnomalyAlertsLambdaRole.name]
}

resource "aws_iam_policy_attachment" "GetSecretValueLambdaPolicyAttachment" {
  name       = "GetSecretValueLambdaPolicyAttachment"
  policy_arn = aws_iam_policy.GetSecretValueLambdaPolicy.arn
  roles      = [aws_iam_role.CostAnomalyAlertsLambdaRole.name]
}

