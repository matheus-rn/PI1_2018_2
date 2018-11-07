from django import forms
from projeto_integrador.models import *

# Slot
class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = ['medicine', 'number']