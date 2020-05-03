from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    tel = models.CharField(max_length=10)
    adresse = models.CharField(max_length=100)
    foyer = models.IntegerField()
    
    def __str__(self):
        return self.nom
    

