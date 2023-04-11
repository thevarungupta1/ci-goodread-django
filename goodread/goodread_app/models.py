from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
