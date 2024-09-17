from rest_framework import serializers
from .models import Product
from genres.serializers import GenresNameSerializer
from sellers.serializers import SellersEnterpriseNameSerializer


class ProductsSerializer(serializers.ModelSerializer):
    seller = SellersEnterpriseNameSerializer()
    genres = GenresNameSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        

