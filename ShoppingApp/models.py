from django.db import models

# Create your models here.

class Shopper(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
    cost = models.IntegerField()
    items = models.CharField(max_length=80)
    shippingTime = models.IntegerField()
    sale = models.BooleanField()
    Buyer = models.ForeignKey(Shopper, related_name="purchases", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)