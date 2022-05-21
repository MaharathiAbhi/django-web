from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

routers = DefaultRouter()
routers.register('Msg', views.exam, basename='msg')
routers.register('Register', views.register, basename='register')


urlpatterns = [
    path('', include(routers.urls)),
    path('auth/login/', obtain_auth_token, name='create-token')
]
