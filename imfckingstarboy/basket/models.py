from django.db import models
from shop.models import Book

# Create your models here.

class Order(models.Model):
    #product_fk = models.ForeignKey(Book, on_delete=models.CASCADE)
    #product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #quantity = models.IntegerField()
    items = models.TextField(null=True)

    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def formatted_order_date(self):
        return self.created.strftime("%d.%m.%Y. - %H:%M") 
    
    def __str__(self):
        return f"Order {self.full_name}, {self.city}, {self.formatted_order_date()}, cena: {self.price}"
