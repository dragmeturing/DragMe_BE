from tastypie.resources import ModelResource
from api.models import Show
from api.models import Venue
from tastypie.authorization import Authorization

class ShowResource(ModelResource):
    class Meta:
        queryset = Show.objects.all()
        resource_name = 'show'
        authorization = Authorization()

class VenueResource(ModelResource):
    class Meta:
        queryset = Venue.objects.all()
        resource_name = 'venue'
        authorization = Authorization()
