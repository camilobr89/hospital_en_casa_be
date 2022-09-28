from django.db import models
from .user import User
from .family import Family
from .medical import Medical
from .nurse import Nurse
from .history import History

class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    medical = models.ForeignKey(Medical, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)