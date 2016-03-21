from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Ticket(models.Model):
    number = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.number

class TicketComment(models.Model):
    ticket = models.ForeignKey(
        'Ticket',
        on_delete=models.CASCADE
    )

class TicketFile(models.Model):
    ticket = models.ForeignKey(
        'Ticket',
        on_delete=models.CASCADE
    )
