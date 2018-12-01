from django.test import TestCase
from projeto_integrador.models import Slot, Medicine
from unittest import mock
from datetime import date

class slotTestCase(TestCase):

    def setUp(self):
        Slot.objects.create(number = 2)


    def testSlotExist(self):
        slot = Slot.objects.get(number = 2)
        slot=slot.number
        self.assertEqual(slot,2)

class MedicinetTestCase(TestCase):
    def setUp(self):
        Slot.objects.create(number = 2)
        slot=Slot.objects.get(number = 2) 

        Medicine.objects.create(name='PI',interval="13:10:00",initial_time="20:00:00",
                                amount=10,limit="00:10:00",status=True,slot=slot
                                )
    def testsMedicineExist(self):
        medicine=Medicine.objects.get(name="PI")
        self.assertEqual(medicine.name,"PI")