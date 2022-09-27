from django.db import models
from .user import User
from .family import Family
from .medical import Medical
from .nurse import Nurse
from .history import History

class Patient(models.Model):
    id = models.BigIntegerField('Cedula', primary_key=True)
    user_id = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    family_id = models.ForeignKey(Family, related_name='patient', on_delete=models.CASCADE)
    medical_id = models.ForeignKey(Medical, related_name='patient', on_delete=models.CASCADE)
    nurse_id = models.ForeignKey(Nurse, related_name='patient', on_delete=models.CASCADE)
    history_id = models.ForeignKey(History, related_name='patient', on_delete=models.CASCADE)