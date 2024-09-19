from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import AccountSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from authentication.permission import GlobalPermissionClass





class AccountInfoListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass)
    serializer_class = AccountSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    
    

 




