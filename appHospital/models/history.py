from django.db import models

class History(models.Model):
    id = models.BigAutoField(primary_key=True)
    oximetry = models.IntegerField('Oximetry', default=0)
    breathing_frequency = models.IntegerField('Breathing Frequency', default=0)
    heart_rate = models.IntegerField('Heart Rate', default=0)
    temperature = models.IntegerField('Temperature', default=0)
    blood_pressure = models.IntegerField('Blood Pressure', default=0)
    blood_glucose = models.IntegerField('Blood Glucose', default=0)
    diagnosis = models.CharField('Diagnosis', max_length=50)
    treatment = models.CharField('Treatment', max_length=50)
    