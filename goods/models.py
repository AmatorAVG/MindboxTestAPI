from django.db import models


class Product (models .Model) :
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)
    products = models.ManyToManyField(Product, blank=True)
