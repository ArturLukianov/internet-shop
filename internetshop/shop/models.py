from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)

    # Вес в граммах
    weight = models.IntegerField(null=True, blank=True)

    model = models.CharField(max_length=64, null=True, blank=True)
    processor = models.CharField(max_length=32, null=True, blank=True)
    ram_size = models.IntegerField(null=True, blank=True)  # размер оперативной памяти
    speed = models.FloatField(null=True, blank=True)  # скорость
    battery_capacity = models.IntegerField(null=True, blank=True)  # ёмкость аккумулятора

    def __str__(self):
        return f'{self.name}'