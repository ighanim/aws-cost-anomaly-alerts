resource "aws_lambda_function" "CostAnomalyAlertsLambda" {
  description = "Lambda Function to Send Cost Anomaly Alerts to different channels"
  filename      = "${path.module}/lambda-package-v1.0.0.zip"
  function_name = "CostAnomalyAlertsLambda"
  role          = aws_iam_role.CostAnomalyAlertsLambdaRole.arn
  handler       = "lambda_function.lambda_handler"
  runtime     = "python3.7"
  layers      = [lookup(var.app_config_layer_arn, data.aws_region.current.name, "")]
  timeout     = 15
  
  publish = true
  
  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_lambda_alias" "CostAnomalyAlertsLambdaAliasProd" {
  name             = "prod"
  function_name    = aws_lambda_function.CostAnomalyAlertsLambda.arn
  function_version = "1" 

}

resource "aws_lambda_permission" "CostAnomalyAlertsLambdaSnsPermission" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_alias.CostAnomalyAlertsLambdaAliasProd.arn
  principal     = "sns.amazonaws.com"
  source_arn    = aws_sns_topic.SnsTopicCostAnomaly.arn
}
