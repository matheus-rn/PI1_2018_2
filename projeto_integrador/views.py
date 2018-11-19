from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404

from projeto_integrador.serializers import *
from projeto_integrador.models import *
from projeto_integrador.forms import *

#rest_framework imports
from rest_framework import generics, views, viewsets, status
from rest_framework.response import Response


def home(request):
    return  render(request,'home.html')

# Medicamento
class MedicamentoViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class MedicamentoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


def medicamentoIndexView(request):
    queryset = Medicamento.objects.all()
    context = {
        "medicamentos": queryset,
    }

    return render(request, 'medicamentoIndex.html', context)


def medicamentoDetailView(request, medicamento_id):
    try:
        medicamento = Medicamento.objects.get(pk=medicamento_id)
    except Medicamento.DoesNotExist:
        raise Http404("O medicamento não existe")
    return render(request, 'medicamentoDetail.html', {'medicamento': medicamento})


# Slot
def list_slots(request):
    slots = Slot.objects.all()
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