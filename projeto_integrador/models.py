from django.db import models


class Slot(models.Model):
    # medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE)
    medicine = models.CharField(max_length=20)
    number = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.number
