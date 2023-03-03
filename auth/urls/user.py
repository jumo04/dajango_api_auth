from django.conf.urls import url
from auth.views.user import user


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', user.api_user_detail, name='api_user_detail'),
]