from django.shortcuts import render , redirect
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
# slug 16 dfsd-sdfsdf-sdfd-dfsd
from rest_framework.views import APIView , status
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.parsers import MultiPartParser



def HomePage(request):
    return render(request, "home.html")

class ProductListCreateAPIView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('home-page')  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    def get_object(self):
        id = self.kwargs["id"]
        return get_object_or_404(Product, id=id)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



def showPrdAll(request):
    prod=Product.objects.all()
    return render(request, 'admin_product.html', {'prod': prod})
    

def showPrd(request):
    prodPermission=Product.objects.filter(permission = True)
    return render(request, 'base.html', {'prodPermission': prodPermission})


def add(request):
    return render(request, "add_product.html")
def update_permission(request,id):
    prod =Product.objects.get(id=id)
    permission=not prod.permission

    Product.objects.filter(id=id).update(permission=permission)
    
    return JsonResponse({'message': 'İşlem başarılı'})
