from .serializers import SellersSerializer
from authentication.permission import GlobalPermissionClass
from .models import Seller
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)




class SellersListCreateAPIView(ListCreateAPIView):
    queryset = Seller.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = SellersSerializer





class SellersRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SellersSerializer
    
    