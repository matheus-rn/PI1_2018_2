from django.test import TestCase
from projeto_integrador.models import Slot, Medicine
from datetime import date
from unittest import mock

class slotTestCase(TestCase):
    def setUp(self):
        Slot.objects.create(number = 2)


    def slotExist(self):
        slot = Slot.objects.get(number = 2)
        self.assertTrue(slot)


def fakeSlot():
    return 2


def fakeTimeSeconds():
    return date.seconds(15)


def fakeTimeHour():
    return date.time(15000)


class medicineTestCase(TestCase):
    @mock.patch("date.seconds", fakeTimeSeconds)
    @mock.patch("date.time", fakeTimeHour)
    @mock.patch("Slot", fakeSlot)


    def setUp(self):
        Medicine.objects.create(
            name = "abacate",
            interval = date.seconds(),
            initial_time = date.time(),
            amount = 8,
            limit = date.seconds(),
            status = True,
            slot = Slot()
        )


    def checkExistMedicine(self):
            med = Medicine.objects.get(
                name = "abacate",
                interval = 15,
                initial_time = 15000 ,
                amount = 8,
                limit = 15,
                status = True,
                slot = 2
            )
            self.assertTrue(med)