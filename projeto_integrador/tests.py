from django.test import TestCase
from models import Slot,Medicine
from datetime import date

import mock

class slotTestCase(TestCase):
    def setUp(self):
        Slot.objects.create(number = 2)

    def slotExist(self):
        slot = Slot.objects.get(number = 2)
        self.assertTrue(slot)

def fakeSlot():
    return 2
def fakeTimeSeconds():
    return datetime.seconds(15)
def fakeTimeHour():
    return datetime.time(15000)
class medicineTestCase(TestCase):

        @mock.patch("datetime.date.seconds", fakeTimeSeconds)
        @mock.patch("datetime.date.time", fakeTimeHour)
        @mock.patch("Slot", fakeSlot)
        def setUp(self):
            Medicine.objects.create(name = "abacate",
                                    interval = datetime.date.seconds(),
                                    initial_time = datetime.date.time(),
                                    amount = 8,
                                    limit = datetime.date.seconds(),
                                    status = True,
                                    slot = Slot()
                                    )

        def checkExistMedicine(self):
                med = Medicine.objects.get(name = "abacate",
                                        interval = 15,
                                        initial_time = 15000 ,
                                        amount = 8,
                                        limit = 15,
                                        status = True,
                                        slot = 2
                                        )
                self.assertTrue(med)
