from django.db import models


class Person (models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date=models.DateField()
    bio=models.TextField()
    mail=models.EmailField()
    jabber=models.CharField(max_length=30)
    skype=models.CharField(max_length=30)
    other=models.CharField(max_length=30)

    def __unicode__(self):
        return self.last_name
