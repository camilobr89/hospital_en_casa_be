from django.db import models
from .user import User

class Nurse(models.Model):
    id = models.BigIntegerField('Cedula', primary_key=True)
    user_id = models.ForeignKey(User, related_name='nurse', on_delete=models.CASCADE)
    assistant = models.BooleanField('Assistant', default=False)
    