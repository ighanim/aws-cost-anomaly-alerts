resource "aws_ce_anomaly_monitor" "CostAnomalyMonitor" {
  count = var.create_service_monitor ? 1 : 0
  name  = "cost-anomaly-alerts-monitor"

  monitor_type      = "DIMENSIONAL"
  monitor_dimension = "SERVICE"
}

resource "aws_ce_anomaly_subscription" "AnomalySubscription" {
  count = var.create_service_monitor ? 1 : 0
  name  = "CostAnomalySubscription"

  threshold_expression {
    or {
      dimension {
        key           = "ANOMALY_TOTAL_IMPACT_PERCENTAGE"
        values        = [var.costAnomalyTotalImpactPercentage]
        match_options = ["GREATER_THAN_OR_EQUAL"]
      }
    }

    or {
      dimension {
        key           = "ANOMALY_TOTAL_IMPACT_ABSOLUTE"
        values        = [var.costAnomalyTotalImpactAbsolute]
        match_options = ["GREATER_THAN_OR_EQUAL"]
      }
    }

  }

  //threshold_expression = jsonencode({ "Or": [{ "Dimensions": {"Key": "ANOMALY_TOTAL_IMPACT_PERCENTAGE", "MatchOptions": [ "GREATER_THAN_OR_EQUAL" ], "Values": [ "${costAnomalyTotalImpactPercentage}" ]}},{"Dimensions": {"Key": "ANOMALY_TOTAL_IMPACT_ABSOLUTE","MatchOptions": [ "GREATER_THAN_OR_EQUAL" ],"Values": [ "${costAnomalyTotalImpactAbsolute}" ]}}]})
  frequency        = "IMMEDIATE"
  monitor_arn_list = [aws_ce_anomaly_monitor.CostAnomalyMonitor[0].arn]
  subscriber {
    type    = "SNS"
    address = aws_sns_topic.SnsTopicCostAnomaly.arn
  }

}

