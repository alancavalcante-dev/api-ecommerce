from rest_framework import serializers 
from products.serializers import ProductsSerializer
from .models import Review


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'



class ReviewsSerializerTeste(serializers.ModelSerializer):
    product = ProductsSerializer()

    class Meta:
        model = Review
        fields = ['user', 'product', 'rate']