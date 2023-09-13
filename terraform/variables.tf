variable "default_slack_webhook_url" {
  description = "Default Slack Webhook URL."
  type        = string
  default     = "{your_workspace_webhook_url}"
}

variable "default_teams_webhook_url" {
  description = "Default Teams Webhook URL."
  type        = string
  default     = "{your_ms_teams_webhook_url}"

}

variable "display_account_name_enabled" {
  description = "Select whether to display Account Name in the Notification or not."
  type        = bool
  default     = true
}

variable "create_service_monitor" {
  description = "If true then the Service Monitor will be created with the Terraform stack."
  type        = bool
  default     = true
}

variable "costAnomalyTotalImpactAbsolute" {
  description = "Absolute threshold for cost anomaly subscription."
  type        = string
  default     = "100"
}

variable "costAnomalyTotalImpactPercentage" {
  description = "Percentage-based threshold for cost anomaly subscription."
  type        = string
  default     = "40"
}

