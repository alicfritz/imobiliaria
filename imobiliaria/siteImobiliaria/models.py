from django.db import models

# Create your models here.

class Imoveis(models.Model):
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    area = models.DateField()
    bedrooms = models.IntegerField()
    bathrooms= models.IntegerField()
    floor = models.IntegerField()
    parking = models.CharField(max_length=100)
    value = models.IntegerField()
    type = models.CharField(max_length=100)
    path = models.DateField()