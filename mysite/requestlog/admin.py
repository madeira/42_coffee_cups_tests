from django.contrib import admin
from mysite.requestlog.models import RequestLog


def priority_increase(modeladmin, request, queryset):
    queryset.update(status='1')
priority_increase.short_description = "Increase status"


def priority_lower(modeladmin, request, queryset):
    queryset.update(status='0')
priority_lower.short_description = "Lower status"


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip', 'status']
    actions = [priority_increase, priority_lower]
    list_filter = ['status']

admin.site.register(RequestLog, RequestLogAdmin)
