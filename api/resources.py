from tastypie.resources import ModelResource
from api.models import Show
from tastypie.authorization import Authorization

class ShowResource(ModelResource):
    class Meta:
        queryset = Show.objects.all()
        resource_name = 'show'
        authorization = Authorization()
