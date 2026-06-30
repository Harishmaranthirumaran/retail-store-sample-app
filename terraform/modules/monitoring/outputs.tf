output "prometheus_workspace_id" {
  description = "Amazon Managed Prometheus workspace ID"
  value       = var.enable_amazon_managed_prometheus ? "enabled" : "disabled"
}

output "grafana_workspace_id" {
  description = "Amazon Managed Grafana workspace ID"
  value       = var.enable_amazon_managed_grafana ? "enabled" : "disabled"
}
