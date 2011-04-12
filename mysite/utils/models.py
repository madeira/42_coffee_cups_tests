from django.db import models
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import Message
from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from mysite.requestlog.models import RequestLog

ACTION_CHOICES = {
    True: 'create',
    False: 'edit',
    None: 'delete'}


class Signal(models.Model):
    model_name = models.CharField(max_length=100)
    action = models.CharField(max_length=10,
                              choices=(('create', 'Create'),
                                       ('edit', 'Edit'),
                                       ('delete', 'Delete')))


def action_signals(sender, **kwargs):
    if sender not in (Signal, Message, Session, LogEntry, RequestLog):
        Signal.objects.create(model_name=str(sender.__name__),
                             action=ACTION_CHOICES[kwargs.get('created')])

post_save.connect(action_signals)
post_delete.connect(action_signals)
