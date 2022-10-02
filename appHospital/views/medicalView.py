from lib2to3.pgen2 import token
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from appHospital.models.user import User
from appHospital.serializers.medicalSerializer import MedicalSerializer
from appHospital.serializers.userSerializer import UserSerializer
from appHospital.models.medical import Medical

class MedicalListCreateView(views.APIView):

    def get(self, request):
        medicals = Medical.objects.all()
        serializer = MedicalSerializer(medicals, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a medico")
        userData = request.data.get('user')
        serializerU = UserSerializer(data=userData)
        serializerU.is_valid(raise_exception=True)
        user = serializerU.save()
        enfData = request.data
        enfData.update({'user': user.id})
        serializerEnf = MedicalSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()

        tokenData = {
            'username': userData.get('username'),
            'password': userData.get('password')
        }

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


class MedicalRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    

    def get(self, obj):
        user = User.objects.get(id=obj.id)
        medical = Medical.objects.get(user=obj.id)
        return{
            "user": {
                "id": user.id,
                "rol": user.rol,
                "name": user.name,
                "last_name": user.last_name,
                "cellphone": user.cellphone,
                "email": user.email,
                "address": user.address,
                "username": user.username,
                "password": user.password
            },
            "specialty": medical.specialty
        }
            
        
  


