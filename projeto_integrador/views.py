from django.shortcuts import render,HttpResponse

def home(request):
    return  render(request,'projeto_integrador/home.html')