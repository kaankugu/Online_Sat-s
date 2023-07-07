from django.urls import path, include
from kullanici import views as kullaniciViews
from kullanici import urls 
from rest_framework.routers import DefaultRouter
from django.contrib import admin

router = DefaultRouter()
router.register(r'kimlik', kullaniciViews.KimlikViewSet, basename='kimlik')


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('/', kullaniciViews.KullaniciGirisView.as_view(), name='kullanici-giris'),
    path('cikis/', kullaniciViews.KullaniciCikisView.as_view(), name='kullanici-cikis'),
    path('kayıt/', kullaniciViews.KullaniciKayitView.as_view(), name='kullanici-kayıt'),
    path('', include(router.urls)),





]

