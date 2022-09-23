from django.db import models
from .user import User

class Medical(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='nurse', on_delete=models.CASCADE)
    specialty = models.CharField('Specialty', max_length=50)