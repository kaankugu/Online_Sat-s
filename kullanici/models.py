from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Kullanici(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_set', blank=True
    )


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class kimlik(models.Model):
    username = models.CharField(max_length=20)
    pasaport = models.CharField(max_length=20)
    def __str__(self):
        return self.username