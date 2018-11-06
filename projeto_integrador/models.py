from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nome = models.CharField(max_length=20)
    intervalo = models.TimeField()
    horario_Ini = models.TimeField()
    qtd = models.PositiveIntegerField(blank=False, null=False)
    limite = models.PositiveIntegerField(blank=False, null=False)
    status = models.BooleanField(default=True)
