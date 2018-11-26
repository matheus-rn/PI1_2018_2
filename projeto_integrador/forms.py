from django import forms
from projeto_integrador.models import *


# Medicine
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


# Slot
class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'
