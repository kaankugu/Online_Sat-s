from django.urls import path, include
from kullanici import views as kullaniciViews
from kullanici import urls 
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth import views as auth_views
from kullanici import views as kullanici
from products import views as products
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

router = DefaultRouter()


urlpatterns = [    
path('',products.HomePage , name="home-page" ),
path('admin/', admin.site.urls),
path('user/', include('kullanici.urls')),
path("", include("products.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

