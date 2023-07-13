from django.conf import settings
from django.db import models
from rest_framework import status
# from kullanici.models import user
class Product(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='prod_img', default='prod_img/no_image.png')
    permission = models.BooleanField(default=False)
    # user=models.
    # slug=models.Slugfield(default=)
    
    # slug=m.CharField(uuid)

    def __str__(self):
        return self.title
    # def model save method:
    #    rnd= random string method
    #     slug=title+"_"+rnd

