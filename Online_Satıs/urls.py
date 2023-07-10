from django.urls import path, include
from kullanici import views as kullaniciViews
from kullanici import urls 
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth import views as auth_views
from kullanici import views as kullanici
from products import views as products


router = DefaultRouter()


urlpatterns = [    
path('',products.HomePage , name="home page" ),
path('admin/', admin.site.urls),
path('', include('kullanici.urls')),
path("", include("products.urls")),
]

