from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    published_date= models.DateField()
