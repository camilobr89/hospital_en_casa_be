from django.db import models
from .user import User

class Family(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50)
   