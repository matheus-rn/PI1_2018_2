from django import forms
from .models import Slot


# Slot
class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'
