from appHospital.models.medical import Medical
from rest_framework import serializers

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = ['specialty']