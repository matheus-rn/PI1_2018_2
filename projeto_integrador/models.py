from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medicamento(models.Model):
    nomeMedicamento = models.CharField(max_length=20)
    horarios = models.TimeField()
    nomeMedicado = models.CharField(max_length=20)
    dosagemMedicamento = models.CharField(max_length=10)
    intervaloHorario = models.TimeField()
