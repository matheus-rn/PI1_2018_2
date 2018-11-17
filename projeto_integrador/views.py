from django.shortcuts import render, HttpResponse
from django.http import Http404

from projeto_integrador.serializers import *
from projeto_integrador.models import *

#rest_framework imports
from rest_framework import generics,views,viewsets, status
from rest_framework.response import Response


def home(request):
    return  render(request,'home.html')


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
