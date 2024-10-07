from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class AccountSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
