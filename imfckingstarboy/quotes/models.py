from django.db import models

# Create your models here.

class Quote(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return self.text