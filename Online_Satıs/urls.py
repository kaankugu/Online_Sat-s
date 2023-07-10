from django.urls import path, include
from kullanici import views as kullaniciViews
from kullanici import urls 
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth import views as auth_views


router = DefaultRouter()


urlpatterns = [    
path('admin/', admin.site.urls),
path('', include('kullanici.urls')),
]

