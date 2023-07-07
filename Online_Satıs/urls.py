from django.urls import path, include
from kullanici import views as kullaniciViews
from kullanici import urls 
from django.contrib import admin

urlpatterns = [

    path('admin/', admin.site.urls),
    path('giris/', kullaniciViews.KullaniciGirisView.as_view(), name='kullanici-giris'),
    path('cikis/', kullaniciViews.KullaniciCikisView.as_view(), name='kullanici-cikis'),
]

