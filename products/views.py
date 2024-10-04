from authentication.permission import GlobalPermissionClass
from rest_framework.filters import SearchFilter
from .serializers import ProductsSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (

    # Admins
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,

    # Clients
    ListAPIView,
    RetrieveAPIView
)



class ProductsListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'seller__enterprise_name', 'genres__name']
    


class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'seller__enterprise_name', 'genres__name']  






class ProductsRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer



class ProductsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ProductsSerializer
    
    