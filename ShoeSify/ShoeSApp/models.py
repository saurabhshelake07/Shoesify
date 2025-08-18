from django.db import models

# Create your models here.
class ShoeModel(models.Model):
    name = models.CharField(max_length=60)
    brand = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    gender = models.CharField(max_length=60)
    size = models.IntegerField()
    stock = models.IntegerField()
    price = models.FloatField()