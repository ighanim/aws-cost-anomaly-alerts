resource "aws_appconfig_application" "CostAnomalyAlertsApplication" {
  name        = "cost-anomaly-alerts-application"
  description = "Cost Anomaly Alerts AppConfig Application"

}

resource "aws_appconfig_environment" "CostAnomalyAlertsEnvironment" {
  name           = "cost-anomaly-alerts-environment"
  application_id = aws_appconfig_application.CostAnomalyAlertsApplication.id
  description    = "Cost Anomaly to Alerts AppConfig Application Environment"

}

resource "aws_appconfig_configuration_profile" "CostAnomalyAlertsConfigProfile" {
  name           = "cost-anomaly-alerts-configuration-profile"
  application_id = aws_appconfig_application.CostAnomalyAlertsApplication.id
  description    = "Cost Anomaly Alerts AppConfig Application Environment"
  location_uri   = "hosted"

}

resource "aws_appconfig_hosted_configuration_version" "CostAnomalyAlertsConfigVersion" {
  application_id           = aws_appconfig_application.CostAnomalyAlertsApplication.id
  configuration_profile_id = aws_appconfig_configuration_profile.CostAnomalyAlertsConfigProfile.configuration_profile_id
  content_type             = "application/json"
  content = jsonencode({
    feature-flags = {
      displayAccountName = var.display_account_name_enabled
    }
    routing-configurations = [{
      default = true
      target-channels = [{
        type = "MS_Teams"
        URL  = var.default_teams_webhook_url
        }, {
        type = "Slack"
        URL  = var.default_slack_webhook_url
      }]
    }]
  })


}

resource "aws_appconfig_deployment_strategy" "CostAnomalyAlertsDeploymentStrategy" {
  name                           = "cost-anomaly-alerts-deployment-strategy"
  description                    = "Cost Anomaly Alerts Deployment Strategy"
  deployment_duration_in_minutes = 1
  final_bake_time_in_minutes     = 1
  growth_factor                  = 100
  growth_type                    = "LINEAR"
  replicate_to                   = "NONE"

  tags = {
    Project = "CostAnomalyAlerts"
  }
}

resource "aws_appconfig_deployment" "CostAnomalyAlertsDeployment" {
  application_id           = aws_appconfig_application.CostAnomalyAlertsApplication.id
  configuration_profile_id = aws_appconfig_configuration_profile.CostAnomalyAlertsConfigProfile.configuration_profile_id
  configuration_version    = aws_appconfig_hosted_configuration_version.CostAnomalyAlertsConfigVersion.version_number
  deployment_strategy_id   = aws_appconfig_deployment_strategy.CostAnomalyAlertsDeploymentStrategy.id
  environment_id           = aws_appconfig_environment.CostAnomalyAlertsEnvironment.environment_id
  description              = "Cost Anomaly Alerts Deployment"

  tags = {
    Project = "CostAnomalyAlerts"
  }
}