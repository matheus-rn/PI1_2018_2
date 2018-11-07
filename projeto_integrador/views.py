from django.shortcuts import render,HttpResponse

from projeto_integrador.serializers import *
from projeto_integrador.models import *

#rest_framework imports
from rest_framework import generics,views,viewsets, status
from rest_framework.response import Response

def home(request):
    return  render(request,'projeto_integrador/home.html')

class MedicamentoViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class MedicamentoDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
