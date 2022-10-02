from django.db import models
from .user import User

class Nurse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assistant = models.BooleanField(default=False)
    