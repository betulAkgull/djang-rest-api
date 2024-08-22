
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import TestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    path('api/test/',TestView.as_view(),name = 'test'),
    path('api/token/', obtain_auth_token, name = 'obtain-token'),
    path('rest-auth/', include('rest_framework.urls')),
]
