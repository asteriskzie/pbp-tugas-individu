from django.db import models

# Create your models here.
class Jam(models.Model) : 
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()