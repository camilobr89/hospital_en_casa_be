from appHospital.models.nurse import Nurse
from rest_framework import serializers

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['assistant']