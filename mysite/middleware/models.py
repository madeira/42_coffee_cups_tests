from django.db import models


class Middlewares(models.Model):
    user_ip=models.CharField(max_length=100)
    link_come=models.TextField
    user_agent=models.CharField(max_length=100)
    host=models.CharField(max_length=100)

    def __unicode__(self):
        return self.user_ip
