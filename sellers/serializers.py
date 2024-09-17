from rest_framework import serializers 
from .models import Seller


class SellersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = '__all__'


class SellersEnterpriseNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ['enterprise_name']