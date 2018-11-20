from __future__ import unicode_literals
from django.db import models


class Slot(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.number


class Medicine(models.Model):
    name = models.CharField(max_length=20)
    interval = models.TimeField()
    initial_time = models.TimeField()
    amount = models.PositiveIntegerField(blank=False, null=False)
    limit = models.TimeField()
    status = models.BooleanField(default=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name