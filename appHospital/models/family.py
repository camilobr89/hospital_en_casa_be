from django.db import models
from .user import User

class Family(models.Model):
    id = models.BigIntegerField('Cedula', primary_key=True)
    user_id = models.ForeignKey(User, related_name='family', on_delete=models.CASCADE)
    relationship = models.CharField('Relationship', max_length=50)
   