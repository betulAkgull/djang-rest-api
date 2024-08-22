
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import PostView,PostCreateView,PostListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')), 
    #path('api/test/',TestView.as_view(),name = 'test'),
    path('api/token/', obtain_auth_token, name = 'obtain-token'),
    path('rest-auth/', include('rest_framework.urls')),
    path('api/post/',PostView.as_view(),name='post'),
    path('api/create/',PostCreateView.as_view(),name='create'),
    path('api/list/',PostListCreateView.as_view(),name='list'),
]
