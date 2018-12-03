from django.test import TestCase, Client
from projeto_integrador.models import Slot, Medicine
from unittest import mock
from datetime import date


class slotTestCase(TestCase):

    def setUp(self):
        Slot.objects.create(number=2)

    def testSlotExist(self):
        slot = Slot.objects.get(number=2)
        slot = slot.number
        self.assertEqual(slot, 2)


class MedicinetTestCase(TestCase):
    def setUp(self):
        Slot.objects.create(number=2)
        slot = Slot.objects.get(number=2)

        Medicine.objects.create(name='PI', interval="13:10:00", initial_time="20:00:00",
                                amount=10, limit="00:10:00", status=True, slot=slot
                                )

    def testsMedicineExist(self):
        medicine = Medicine.objects.get(name="PI")
        self.assertEqual(medicine.name, "PI")


class StatusCodeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def testStatusIndex(self):
        self.response = self.client.get(
            '/')
        self.assertEqual(self.response.status_code, 200)

    def testStatusMedicine(self):
        self.response = self.client.get(
            '/medicines/')
        self.assertEqual(self.response.status_code, 200)

    def testStatusNewMedicine(self):
        self.response = self.client.get(
            '/new_medicine/')
        self.assertEqual(self.response.status_code, 200)
    
    def testStatusSlots(self):
        self.response = self.client.get(
            '/slots/')
        self.assertEqual(self.response.status_code, 200)
    
    def testStatusNewSlot(self):
        self.response = self.client.get(
            '/new_slot/')
        self.assertEqual(self.response.status_code, 200)
    