from pickle import OBJ
from rest_framework import serializers
from appHospital.models.user import User
from appHospital.models.patient import Patient
from appHospital.models.medical import Medical
from appHospital.models.nurse import Nurse
from appHospital.models.history import History
from appHospital.serializers.patientSerializer import PatientSerializer
from appHospital.serializers.medicalSerializer import MedicalSerializer
from appHospital.serializers.nurseSerializer import NurseSerializer
from appHospital.serializers.historySerializer import HistorySerializer

class UserSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    medical = MedicalSerializer()
    nurse = NurseSerializer()
    history = HistorySerializer()

    class Meta:
        model = User
        fields = ['id', 'rol', 'name', 'last_name', 'cellphone', 'email', 'address', 'username', 'password', 'patient', 'medical', 'nurse', 'history']

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        medical_data = validated_data.pop('medical')
        nurse_data = validated_data.pop('nurse')
        history_data = validated_data.pop('history')
        user = User.objects.create(**validated_data)
        Patient.objects.create(user=user, **patient_data)
        Medical.objects.create(user=user, **medical_data)
        Nurse.objects.create(user=user, **nurse_data)
        History.objects.create(user=user, **history_data)
        return user

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        patient = Patient.objects.get(user=obj.id)
        medical = Medical.objects.get(user=obj.id)
        nurse = Nurse.objects.get(user=obj.id)
        history = History.objects.get(user=obj.id)
        return {
                'id': user.id,
                'rol': user.rol,
                'name': user.name,
                'last_name': user.last_name,
                'cellphone': user.cellphone,
                'email': user.email,
                'address': user.address,
                'username': user.username,
                'password': user.password,
                'patient': {
                    'id': patient.id,
                    'user': patient.user,
                    'blood_type': patient.blood_type,
                    'allergies': patient.allergies,
                    'chronic_diseases': patient.chronic_diseases,
                    'weight': patient.weight,
                    'height': patient.height,
                    'birth_date': patient.birth_date,
            }
        }
 
