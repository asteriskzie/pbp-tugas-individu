from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self) : 
        return self.name + f"<{self.id}>"