"""PI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from projeto_integrador.views import *
from projeto_integrador import urls

urlpatterns = [
    path('',home),
    url(r'^index/', medicamentoIndexView, name='medicamentoIndexView'),
    url(r'^medicamento/(?P<medicamento_id>[0-9]+)/details/$', medicamentoDetailView, name='medicamentoDetailView'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('projeto_integrador.urls')),
]
