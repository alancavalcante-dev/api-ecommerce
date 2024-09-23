from rest_framework.serializers import ModelSerializer
from .models import CartItem
from products.serializers import ProductsSerializer

class CartItemSerializer(ModelSerializer):
    #product = ProductsSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'