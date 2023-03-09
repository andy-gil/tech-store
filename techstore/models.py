from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200, null="true")
    item_desc = models.CharField(max_length=200, null="true")
    item_price = models.CharField(max_length=200, null="true")
    item_image = models.CharField(max_length=200, default="")

class Laptops(models.Model):
    def __str__(self):
        return self.laptops_name

    laptops_name = models.CharField(max_length=200, null="true")
    laptops_desc = models.CharField(max_length=200, null="true")
    laptops_price = models.CharField(max_length=200, null="true")
    laptops_image = models.CharField(max_length=200, default="")

class Desktops(models.Model):
    def __str__(self):
        return self.desktops_name

    desktops_name = models.CharField(max_length=200, null="true")
    desktops_desc = models.CharField(max_length=200, null="true")
    desktops_price = models.CharField(max_length=200, null="true")
    desktops_image = models.CharField(max_length=200, default="")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    laptops = models.ManyToManyField(Laptops, blank=True)
    desktops = models.ManyToManyField(Desktops, blank=True)

