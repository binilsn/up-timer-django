from core.form import BaseForm
from monitors.models import Monitor


class MonitorForm(BaseForm):
    class Meta:
        model = Monitor

        fields = ["name", "url", "interval_seconds"]
