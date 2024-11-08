from netbox.plugins import PluginConfig
from .models import ComponentCollector
import prometheus_client


class PromMetricsConfig(PluginConfig):
    name = 'prom_metrics'
    verbose_name = 'Custom Prometheus Metrics'
    version = '0.1'
    description = 'For testing purposes only'
    base_url = 'prom-metrics'
    min_version = '3.0'
    max_version = '4.2'

    def ready(self):
        super().ready()
        prometheus_client.REGISTRY.register(ComponentCollector())


config = PromMetricsConfig
