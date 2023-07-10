from django.urls import path
import kullanici.views as views
from kullanici.views import UserList,RegisterAPI
from .views import LoginAPI
from knox import views as knox_views


app_name = 'kullanici'

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('users/', UserList.as_view(), name='user-list'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
