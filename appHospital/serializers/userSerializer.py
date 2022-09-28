
from rest_framework import serializers
from appHospital.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','rol', 'name', 'last_name', 'cellphone', 'email', 'address', 'username', 'password']


 
