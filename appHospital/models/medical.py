from django.db import models
from .user import User

class Medical(models.Model):
    id = models.BigIntegerField('Cedula', primary_key=True)
    user_id = models.ForeignKey(User, related_name='medical', on_delete=models.CASCADE)
    specialty = models.CharField('Specialty', max_length=50)