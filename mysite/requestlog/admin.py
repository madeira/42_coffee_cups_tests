from django.contrib import admin
from mysite.requestlog.models import RequestLog


def priority_increase(modeladmin, request, queryset):
    queryset.update(priority=True)
priority_increase.short_description = "Increase status"


def priority_lower(modeladmin, request, queryset):
    queryset.update(priority=False)
priority_lower.short_description = "Lower status"


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip', 'priority']
    actions = [priority_increase, priority_lower]
    list_filter = ['priority']

admin.site.register(RequestLog, RequestLogAdmin)
