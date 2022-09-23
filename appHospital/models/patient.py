from django.db import models
from .user import User
from .medical import Medical
from .nurse_patient import Nurse_patient
from .history import History

class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    medical_id = models.ForeignKey(Medical, related_name='patient', on_delete=models.CASCADE)
    nurse_id = models.ForeignKey(Nurse_patient, related_name='patient', on_delete=models.CASCADE)
    history_id = models.ForeignKey(History, related_name='patient', on_delete=models.CASCADE)