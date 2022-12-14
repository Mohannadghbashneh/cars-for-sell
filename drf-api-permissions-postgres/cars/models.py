from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Car(models.Model):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    rank=models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller= models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.seller