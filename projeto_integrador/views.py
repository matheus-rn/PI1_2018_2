from django.shortcuts import render, HttpResponse, redirect

from projeto_integrador.resources import *
from projeto_integrador.models import *
from projeto_integrador.forms import *


def home(request):
    return  render(request,'home.html')

# Medicine
def list_medicines(request):
    medicines = Medicine.objects.all().order_by('name')
    return render(request, 'medicines.html', {'medicines': medicines})

def detailing_medicines(request, id):
    medicine = Medicine.objects.get(id=id)
    return render(request, 'medicamentoDetail.html', {'medicine': medicine})

def list_medicines_history(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicamentoIndex.html', {'medicines': medicines})

def create_medicine(request):
    form = MedicineForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_medicines')

    return render(request, 'medicine-form.html', {'form': form})


def update_medicine(request, id):
    medicine = Medicine.objects.get(id=id)
    form = MedicineForm(request.POST or None, instance=medicine)

    if form.is_valid():
        form.save()
        return redirect('list_medicines')

    return render(request, 'medicine-form.html', {'form': form})


def delete_medicine(request, id):
    medicine = Medicine.objects.get(id=id)

    if request.method == 'POST':
        medicine.delete()
        return redirect('list_medicines')

    return render(request, 'medicine-delete-confirm.html', {'medicine': medicine})


# Slot
def list_slots(request):
    slots = Slot.objects.all().order_by('number')
    return render(request, 'slots.html', {'slots': slots})


def create_slot(request):
    form = SlotForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_slots')

    return render(request, 'slot-form.html', {'form': form})


def update_slot(request, id):
    slot = Slot.objects.get(id=id)
    form = SlotForm(request.POST or None, instance=slot)

    if form.is_valid():
        form.save()
        return redirect('list_slots')

    return render(request, 'slot-form.html', {'form': form, 'slot': slot})


def delete_slot(request, id):
    slot = Slot.objects.get(id=id)

    if request.method == 'POST':
        slot.delete()
        return redirect('list_slots')

    return render(request, 'slot-delete-confirm.html', {'slot': slot})