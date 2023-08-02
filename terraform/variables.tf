variable "code_package" {
  description = "S3 key for the Lambda Code."
  type        = string
  default     = "costaaaaa"
}

variable "default_slack_webhook_url" {
  description = "Default Slack Webhook URL."
  type        = string
  default     = "https://hooks.slack.com/services/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"
}

variable "default_teams_webhook_url" {
  description = "Default Teams Webhook URL."
  type        = string
  default     = "https://teams"

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
  default     = "1"
}

variable "costAnomalyTotalImpactPercentage" {
  description = "Percentage-based threshold for cost anomaly subscription."
  type        = string
  default     = "1"
}

