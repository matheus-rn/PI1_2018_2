from __future__ import unicode_literals
from django.db import models


class Slot(models.Model):
    number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.number


class Medicamento(models.Model):
    nome = models.CharField(max_length=20)
    intervalo = models.TimeField()
    horario_Ini = models.TimeField()
    qtd = models.PositiveIntegerField(blank=False, null=False)
    limite = models.TimeField()
    status = models.BooleanField(default=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)