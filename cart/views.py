from .serializers import CartItemSerializer
from rest_framework import generics
from .models import CartItem
from rest_framework.permissions import IsAuthenticated
from authentication.permission import GlobalPermissionClass
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem
from products.models import Product


class CartItemListAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)

    def get_queryset(self):
        return CartItem.objects.filter(cart__user__id=self.request.user.id)
    


class AddToCartView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Produto não encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Verifica se o produto já está no carrinho
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity = int(quantity)
        cart_item.save()

        return Response({'message': 'Produto adicionado ao carrinho'}, status=status.HTTP_200_OK)



class QuantityCardItem(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cart_items_numbers = CartItem.objects.filter(
            cart__user__id=request.user.id).count()

        return Response({'quantity': cart_items_numbers}, status=status.HTTP_200_OK)



class CartItemDestroyAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
