from django.db import models
from django.conf import settings


class RequestLog(models.Model):
    user_ip = models.CharField(max_length=100)
    link_come = models.TextField()
    user_agent = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    priority = models.BooleanField(default=settings.REQUESTLOG_DEFAULT_PRIORITY)

    def __unicode__(self):
        return self.user_ip
