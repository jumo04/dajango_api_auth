
from django.conf.urls import url, include
from django.contrib import admin, user

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token


# jwtpatterns = [
#     url(r'^jwt/refresh-token/', refresh_jwt_token, name='refresh_jwt_token'),
#     url(r'^jwt/api-token-verify/', verify_jwt_token, name='verify_jwt_token'),
#     url(r'^jwt/api-token-auth/', obtain_jwt_token, name='obtain_jwt_token'),
# ]

urlpatterns = [
    url(r'^user/$', user.api_admin_user_index, name='api_admin_user_index'),
]