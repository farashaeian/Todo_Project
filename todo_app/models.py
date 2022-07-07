from django.db import models
from datetime import date


class Task(models.Model):
    title = models.TextField(blank=False, null=False)
    description = models.TextField()
    done = models.BooleanField(default=False)
    creation_date = models.DateField(default=date.today(), blank=False, null=False)
    deadline_date = models.DateTimeField(blank=False, null=False)

    class Meta:
        ordering = ['deadline_date']

