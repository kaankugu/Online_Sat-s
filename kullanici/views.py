from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from kullanici.serializers import SnippetSerializer

from rest_framework.response import Response
from rest_framework import status
from kullanici.serializers import KullaniciSerializer
from rest_framework import viewsets
from kullanici.models import Kullanici, kimlik
from kullanici.models import Snippet
from kullanici.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class KullaniciGirisView(APIView):
    def get(self, request):
        # Kullanıcı giriş formunu getirmek için gereken işlemleri gerçekleştirin
        return Response({'message': 'Kullanıcı giriş formu.'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = KullaniciSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                # Kullanıcı doğrulandıysa giriş başarılı yanıtı döndür
                return Response({'message': 'Giriş başarılı.'}, status=status.HTTP_200_OK)
            else:
                # Kullanıcı doğrulanamazsa hatalı giriş yanıtı döndür
                return Response({'message': 'Hatalı kullanıcı adı veya şifre.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Doğrulama başarısızsa hata mesajlarını istemciye gönder
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KullaniciCikisView(APIView):
    def post(self, request):
        # Oturumu sonlandırma işlemlerini gerçekleştir
        # Örneğin: request.user.logout()
        return Response({'message': 'Çıkış başarılı.'}, status=status.HTTP_200_OK)

class KullaniciKayitView(APIView):
    def post(self, request):
        serializer = KullaniciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Kullanıcı kaydedildi.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KimlikViewSet(viewsets.ModelViewSet):
    queryset = kimlik.objects.all().order_by("username")
    serializer_class = KullaniciSerializer


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