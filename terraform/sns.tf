
resource "aws_sns_topic" "SnsTopicCostAnomaly" {
  name = "SnsTopicCostAnomaly"

  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_sns_topic_policy" "SnsTopicPolicyCostAnomaly" {
  arn = aws_sns_topic.SnsTopicCostAnomaly.arn

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid       = "costalerts to publish"
      Effect    = "Allow"
      Principal = { Service = "costalerts.amazonaws.com" }
      Action    = "sns:Publish"
      Resource  = aws_sns_topic.SnsTopicCostAnomaly.arn
      }, {
      Sid       = "Lambda to subscribe"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
      Action    = ["sns:Subscribe", "sns:Receive"]
      Resource  = aws_sns_topic.SnsTopicCostAnomaly.arn
      Condition = {
        StringEquals = {
          "lambda:FunctionArn" = aws_lambda_alias.CostAnomalyAlertsLambdaAliasProd.arn
        }
      }
    }]
  })
}


resource "aws_sns_topic_subscription" "SnsTopcSubscriptionCostAnomaly" {
  topic_arn = aws_sns_topic.SnsTopicCostAnomaly.arn
  protocol  = "lambda"
  endpoint  = aws_lambda_alias.CostAnomalyAlertsLambdaAliasProd.arn
}