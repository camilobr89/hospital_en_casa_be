from appHospital.models.history import History
from rest_framework import serializers

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['oximetry', 'breathing_frequency', 'heart_rate', 'temperature', 'blood_pressure', 'blood_glucose', 'diagnosis', 'treatment']