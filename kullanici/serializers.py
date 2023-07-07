from rest_framework import serializers
from kullanici.models import Kullanici
from .models import Note
from django.contrib.auth.models import User
from kullanici.models import kimlik 



class KullaniciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanici
        fields = ('username', 'password')  
    def create(self, validated_data):
        user = User.objects.create_user(
        username=validated_data['username'],
        password=validated_data['password']
        )
        return user


class KİMLİK(serializers.HyperlinkedModelSerializer):
    class Meta : 
        model = kimlik
        fields = ('username', 'password')  
