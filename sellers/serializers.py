from rest_framework import serializers 
from .models import Seller


class SellersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = '__all__'