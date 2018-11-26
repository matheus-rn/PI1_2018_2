from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from projeto_integrador.models import *


class SlotResource(ModelResource):
    class Meta:
        queryset = Slot.objects.all().order_by('number')
        resource_name = 'slots'
        authorization = Authorization()


class MedicineResource(ModelResource):
    class Meta:
        queryset = Medicine.objects.all().order_by('name')
        resource_name = 'medicines'
        authorization = Authorization()
