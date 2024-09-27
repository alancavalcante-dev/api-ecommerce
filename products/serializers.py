from rest_framework import serializers
from .models import Product
from genres.serializers import GenresNameSerializer
from sellers.serializers import SellersEnterpriseNameSerializer
from django.db.models import Avg


class ProductsSerializer(serializers.ModelSerializer):
    seller = SellersEnterpriseNameSerializer()
    genres = GenresNameSerializer()
    rate = serializers.SerializerMethodField() 

    class Meta:
        model = Product
        fields = '__all__'

    
    def get_rate(self, obj):
        rating_data = obj.filhos.aggregate(rating=Avg('rate'))
        rating = rating_data.get('rating')

        return round(rating, 1) if rating is not None else None


         
        

