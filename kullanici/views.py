from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from kullanici.models import Kullanici, kimlik,Snippet 
from knox.models import AuthToken
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    


def kaydol(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('giris')
    else:
        form = UserCreationForm()
    return render(request, 'kaydol.html', {'form': form})

def giris(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('anasayfa')
    return render(request, 'giris.html')

def cikis(request):
    logout(request)
    return redirect('giris')



class UserList(APIView):
    # Sınıf özelliği olarak serileştirici sınıfını belirtiyoruz
    serializer_class = UserSerializer

    # GET isteklerini işlemek için get() metodunu tanımlıyoruz
    def get(self, request, format=None):
        # Veri kümesini get_queryset() metodunu kullanarak alıyoruz
        users = self.get_queryset()
        # Verileri serileştirmek için get_serializer() metodunu kullanarak bir serileştirici örneği oluşturuyoruz
        serializer = self.serializer_class(users, many=True)
        # Serileştirilmiş verileri Response nesnesi ile döndürüyoruz
        return Response(serializer.data)

    # POST isteklerini işlemek için post() metodunu tanımlıyoruz
    def post(self, request, format=None):
        # İstek verisini serileştirmek için get_serializer() metodunu kullanarak bir serileştirici örneği oluşturuyoruz
        serializer = self.get_serializer(data=request.data)
        # Serileştiriciyi doğruluyoruz
        if serializer.is_valid():
            # Serileştiriciden gelen verilerle bir kullanıcı örneği oluşturuyoruz
            user = User.objects.create_user(**serializer.validated_data)
            # Oluşturulan kullanıcıyı tekrar serileştiriyoruz
            serializer = self.get_serializer(user)
            # Serileştirilmiş kullanıcıyı Response nesnesi ile döndürüyoruz
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Serileştirici geçerli değilse, hataları Response nesnesi ile döndürüyoruz
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Veri kümesini döndüren bir yardımcı metod tanımlıyoruz
    def get_queryset(self):
        # Tüm kullanıcıları döndürüyoruz
        return User.objects.all()
    

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

