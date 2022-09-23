from django.db import models
from .nurse import Nurse
from .patient import Patient

class Nurse_patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    nurse_id = models.ForeignKey(Nurse, related_name='nurse_patient', on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, related_name='nurse_patient', on_delete=models.CASCADE)