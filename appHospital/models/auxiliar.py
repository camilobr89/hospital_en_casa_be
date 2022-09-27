from unicodedata import name
from django.db import models
from .user import User

class Auxiliar(models.Model):
    id = models.BigIntegerField('Cedula', primary_key=True)
    user_id = models.ForeignKey(User, related_name='auxiliar', on_delete=models.CASCADE)
    notas = models.CharField('Notas', max_length=50)
    
