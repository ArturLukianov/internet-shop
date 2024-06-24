from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)
