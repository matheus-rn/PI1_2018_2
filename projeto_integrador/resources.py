from tastypie.resources import ModelResource
from .models import Slot
from tastypie.authorization import Authorization


class SlotResource(ModelResource):
    class Meta:
        queryset = Slot.objects.all().order_by('number')
        resource_name = 'slots'
        authorization = Authorization()
