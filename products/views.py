from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer



def HomePage(request):
    return render(request, "home.html")

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer