from django.conf import settings
from django.db import models

# Create your models here.


class Monitor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="monitors"
    )
    name = models.CharField(max_length=255)
    url = models.URLField()
    interval_seconds = models.PositiveIntegerField(default=300)

    active = models.BooleanField(default=True)

    last_checked_at = models.DateTimeField(null=True, blank=True)
    next_check_at = models.DateTimeField(db_index=True)

    def __str__(self):
        return self.name
