from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    imageLink = models.URLField()
    language = models.CharField(max_length=100)
    pages = models.IntegerField()
    description = models.TextField()