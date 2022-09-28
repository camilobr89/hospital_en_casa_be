from django.db import models
from .user import User

class Medical(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)