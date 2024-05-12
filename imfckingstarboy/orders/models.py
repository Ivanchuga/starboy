from django.db import models
from decimal import Decimal
from django.conf import settings
# Create your models here.



class Order(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
