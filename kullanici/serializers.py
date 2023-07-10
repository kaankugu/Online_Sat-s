from rest_framework import serializers
from kullanici.models import Kullanici,Note,kimlik 
from django.contrib.auth.models import User
from kullanici.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


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
        
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance