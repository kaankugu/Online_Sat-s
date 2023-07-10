from django.urls import path
import  kullanici.views as views


app_name = 'kullanici'

urlpatterns = [
    path('giris/', views.KullaniciGirisView.as_view(), name='kullanici-giris'),
    path('cikis/', views.KullaniciCikisView.as_view(), name='kullanici-cikis'),
    path('kayıt/', views.KullaniciKayitView.as_view(), name='kullanici-cikis'),
    path('kayit/', views.KimlikViewSet.as_view(actions={'post': 'create'}), name='kullanici-kayit'),
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
