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
from django.urls import path, include
from django.conf.urls import include, url
from projeto_integrador.views import *
from projeto_integrador.resources import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    
    # Medicine
    url(r'^api/', include(MedicineResource().urls)),    # /api/medicines/
    path('medicines/', list_medicines, name='list_medicines'),
    path('new_medicine/', create_medicine, name='create_medicine'),
    path('update_medicine/<int:id>/', update_medicine, name='update_medicine'),
    path('delete_medicine/<int:id>/', delete_medicine, name='delete_medicine'),
    path('details_medicines/<int:id>/', detailing_medicines, name='details_medicines'),
    path('medicines_history/', list_medicines_history, name='medicines_history'),

    # Slot 
    url(r'^api/', include(SlotResource().urls)),    # /api/slots/
    path('slots/', list_slots, name='list_slots'),
    path('new_slot/', create_slot, name='create_slot'),
    path('update_slot/<int:id>/', update_slot, name='update_slot'),
    path('delete_slot/<int:id>/', delete_slot, name='delete_slot'),
]
