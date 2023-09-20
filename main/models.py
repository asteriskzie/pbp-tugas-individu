from django.db import models

# Create your models here.
class Item(models.Model) : 
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self) : 
        return self.name