import django_rq
from prometheus_client.metrics_core import GaugeMetricFamily


class ComponentCollector(object):

    def collect(self):
        yield self.get_jobs_metrics()

    @staticmethod
    def get_jobs_metrics():
        netbox_job_count = GaugeMetricFamily("netbox_job_count",
                                             'Number of jobs',
                                             labels=['state', 'queue'])
        for queue_name in django_rq.settings.QUEUES.keys():
            queue = django_rq.get_queue(queue_name)
            netbox_job_count.add_metric(["failed", queue_name], queue.failed_job_registry.count)
            netbox_job_count.add_metric(["started", queue_name], queue.started_job_registry.count)
            netbox_job_count.add_metric(["finished", queue_name], queue.finished_job_registry.count)

        return netbox_job_count
