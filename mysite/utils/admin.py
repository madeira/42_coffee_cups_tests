from django.contrib import admin
from mysite.utils.models import Signal


class SignalAdmin(admin.ModelAdmin):
        list_display = ('model_name', 'action')

admin.site.register(Signal, SignalAdmin)
