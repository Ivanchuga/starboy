from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits= 6, decimal_places=2)
    images = models.ImageField(upload_to="media")
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        print("Tu JEEEEEEEEEEEEEEEEEEE")
        #return reverse('single_book', kwargs={'pk': self.pk})
        return reverse('shop:single_book', args=[str(self.id)])
    

    