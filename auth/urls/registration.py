
from django.conf.urls import url
from auth.views.registration import registration


urlpatterns = [
    url(r'^login/', registration.api_login, name='api_login'),
]