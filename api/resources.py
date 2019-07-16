from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from api.models import Show

class ShowResource(ModelResource):
    class Meta:
        queryset = Show.objects.all()
        resource_name = 'show'
        authorization = Authorization()
