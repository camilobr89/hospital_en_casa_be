from unicodedata import name
from django.db import models
from .user import User

class Auxiliar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notas = models.CharField(max_length=50)
    
