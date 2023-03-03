
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', include('auth.urls.admin')),
    url(r'^auth/', include('auth.urls.registration')),
    url(r'^user/', include('auth.urls.user')),
]