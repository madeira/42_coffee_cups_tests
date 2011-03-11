from django.db import models


class Persone (models.Model):
    first_name=models.CharField()
    last_name=models.CharField()
    date=models.DateField()
    bio=models.TextField()
    mail=models.EmailField()

    def __unicode__(self):
        return self.last_name
