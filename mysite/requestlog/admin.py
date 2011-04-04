from django.contrib import admin
from mysite.requestlog.models import RequestLog


def priority_status(modeladmin, request, queryset):
    for count in queryset:
        if count.status == '1':
            queryset.filter(status='1').update(status='0')
        else:
            queryset.filter(status='0').update(status='1')
priority_status.short_description = "Chenge status"


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_ip', 'status']
    actions = [priority_status]
    list_filter = ['status']

admin.site.register(RequestLog, RequestLogAdmin)
