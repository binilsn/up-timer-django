from django.conf import settings
from django.db import models

# Create your models here.


class MonitorStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    CHECKING = "checking", "Checking"
    UP = "up", "Up"
    DOWN = "down", "Down"
    PAUSED = "paused", "Paused"


class Monitor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="monitors"
    )
    name = models.CharField(max_length=255)
    url = models.URLField()
    interval_seconds = models.PositiveIntegerField(default=300)

    active = models.BooleanField(default=True)

    last_checked_at = models.DateTimeField(null=True, blank=True)
    next_check_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=MonitorStatus, default=MonitorStatus.PENDING
    )

    @property
    def is_paused(self):
        return self.status == MonitorStatus.PAUSED

    @property
    def is_pending(self):
        return self.status == MonitorStatus.PENDING

    @property
    def is_up(self):
        return self.status == MonitorStatus.UP

    @property
    def is_down(self):
        return self.status == MonitorStatus.DOWN

    @property
    def is_checking(self):
        return self.status == MonitorStatus.CHECKING

    def __str__(self):
        return str(self.name)
