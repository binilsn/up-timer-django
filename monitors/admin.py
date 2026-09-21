# Register your models here.
from django.contrib import admin

from .models import Monitor


@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    readonly_fields = (
        "last_checked_at",
        "next_check_at",
    )
    list_display = (
        "name",
        "url",
        "active",
        "interval_seconds",
        "last_checked_at",
        "next_check_at",
    )
    search_fields = ("url", "name")

    list_filter = ("active",)

    ordering = ("name",)
