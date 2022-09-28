from django.db import models

class History(models.Model):
    id = models.BigIntegerField(primary_key=True)
    oximetry = models.IntegerField(default=0)
    breathing_frequency = models.IntegerField(default=0)
    heart_rate = models.IntegerField(default=0)
    temperature = models.IntegerField(default=0)
    blood_pressure = models.IntegerField(default=0)
    blood_glucose = models.IntegerField(default=0)
    diagnosis = models.CharField(max_length=50)
    treatment = models.CharField(max_length=50)
    