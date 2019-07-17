from django.conf.urls import url, include
from django.contrib import admin
from api.resources import ShowResource
from api.resources import VenueResource

show_resource = ShowResource()
venue_resource = VenueResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(show_resource.urls,)),
    url(r'^api/v1/', include(venue_resource.urls)),
]
