from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from projeto_integrador.models import Slot


class SlotResource(ModelResource):
    class Meta:
        queryset = Slot.objects.all().order_by('number')
        resource_name = 'slots'
        authorization = Authorization()
