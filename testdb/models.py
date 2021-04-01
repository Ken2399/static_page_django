from django.db import models

# Create your models here.

class Product(models.Model):
    product_title = models.CharField(max_length=80)
    product_description = models.CharField(max_length=80)
    product_price = models.IntegerField()