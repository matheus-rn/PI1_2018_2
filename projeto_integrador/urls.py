from django.urls import path
from django.conf.urls import url, include
from .views import *
from .resources import *


urlpatterns = [
    path('', home, name='home'),

    # API Slot
    url(r'^api/', include(SlotResource().urls)),

    # Slot
    path('slots', list_slots, name='list_slots'),
    path('new_slot', create_slot, name='create_slot'),
    path('update_slot/<int:id>/', update_slot, name='update_slot'),
    path('delete_slot/<int:id>/', delete_slot, name='delete_slot'),
]
