from django.urls import path
from .views import *


urlpatterns = [
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-create'),
    path('api/products/<int:id>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('allproducts/',  showPrdAll,name="products"),
    path('products/',  showPrd,name="products"),
    path('add/',  add , name ="creatProduct"),
    path('update-permission/<int:id>/',  update_permission , name ="update_permission"),

]