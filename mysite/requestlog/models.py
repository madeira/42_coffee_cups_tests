from django.db import models
from django.conf import settings


class RequestLog(models.Model):
    user_ip = models.CharField(max_length=100)
    link_come = models.TextField()
    user_agent = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default=settings.STATUS)

    def __unicode__(self):
        return self.user_ip
