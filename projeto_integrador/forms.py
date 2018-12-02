from django import forms
from projeto_integrador.models import *


# Medicine
class MedicineForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o nome do medicamento'}))
	interval = forms.TimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o intervalo'}))
	initial_time = forms.TimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite a hora inicial'}))
	amoust = forms.IntegerField(min_value=1, widget=forms.NumberInput(
                attrs={'size':'10'}))
	limit = forms.TimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Digite o limite'}))
	status = forms.BooleanField(widget=forms.CheckboxInput())
	

	class Meta:
		model = Medicine
		fields = ['name','interval','initial_time','amoust','limit', 'status','slot',]


# Slot
class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'
