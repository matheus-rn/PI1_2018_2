from django.shortcuts import render, HttpResponse, redirect
from projeto_integrador.models import *
from projeto_integrador.forms import *

def home(request):
    return render(request, 'projeto_integrador/home.html')


# Slot
def list_slots(request):
    slots = Slot.objects.all()
    return render(request, 'projeto_integrador/slots.html', {'slots':slots})

def create_slot(request):
    form = SlotForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_slots')

    return render(request, 'projeto_integrador/slot-form.html', {'form':form})

def update_slot(request, id):
    slot = Slot.objects.get(id=id)
    form = SlotForm(request.POST or None, instance=slot)

    if form.is_valid():
        form.save()
        return redirect('list_slots')

    return render(request, 'projeto_integrador/slot-form.html', {'form':form, 'slot':slot})

def delete_slot(request, id):
    slot = Slot.objects.get(id=id)

    if request.method == 'POST':
        slot.delete()
        return redirect('list_slots')

    return render(request, 'projeto_integrador/slot-delete-confirm.html', {'slot':slot})