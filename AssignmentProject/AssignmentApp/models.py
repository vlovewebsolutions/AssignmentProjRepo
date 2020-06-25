from django.db import models

# Create your models here.


class Product(models.Model):
    ProductName = models.CharField(max_length=50)
    ProductDesc = models.CharField(max_length=1000)
    ProductQTY = models.PositiveIntegerField()
    ProductPrice = models.PositiveIntegerField()
