from django import forms

from monitors.models import Monitor


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor

        fields = ["name", "url", "interval"]
