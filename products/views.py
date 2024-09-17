from authentication.permission import GlobalPermissionClass
from .serializers import ProductsSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


class ProductsListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer



class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer
    
    