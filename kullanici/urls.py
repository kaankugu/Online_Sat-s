from django.urls import path
import kullanici.views as views
from kullanici.views import RegisterAPI
from .views import *
from knox import views as knox_views




urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register-api'),
    path('api/login/', LoginAPI.as_view(), name='login-api'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path("kayıt",kaydol),
    path("giris",giris,name="giris"),
]
