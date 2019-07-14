from django.conf.urls import url, include
from django.contrib import admin
from api.resources import ShowResource

show_resource = ShowResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(show_resource.urls)),
]
