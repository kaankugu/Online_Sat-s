from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status , viewsets , permissions,generics
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from kullanici.serializers import *
from kullanici.models import *



#from .utils import generate_jwt_token, decode_jwt_token

def get_jwt_token(request):
    # Örnek olarak, bir kullanıcının kimlik bilgilerini kullanarak JWT token oluşturuyoruz
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Kullanıcı kimlik bilgilerinin doğruluğunu kontrol edin ve JWT token oluşturun
    if username == 'admin' and password == 'password':
        payload = {'username': username}
        token = generate_jwt_token(payload)
        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Geçersiz kimlik bilgileri'}, status=401)

def verify_jwt_token(request):
    token = request.POST.get('token')

    try:
        decoded_payload = decode_jwt_token(token)
        username = decoded_payload['username']
        return JsonResponse({'message': f'Token geçerli. Kullanıcı: {username}'})
    except jwt.ExpiredSignatureError:
        return JsonResponse({'error': 'Token süresi doldu'}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({'error': 'Geçersiz token'}, status=401)





class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # İşlem başarılı olduğunda veya hata durumunda uygun bir yanıt döndürebilirsiniz
        return render(request, "login.html")

    

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return render(request, "home.html")
        # return super(LoginAPI, self).post(request, format=None)

def kaydol(request):
    return render(request, "kaydol.html")

def logout(request):
    logout(request)
    return redirect('giris')

def giris(request) : 
    return render(request , "login.html")