from authentication.permission import GlobalPermissionClass
from .serializers import ReviewsSerializer, ReviewsSerializerTeste
from .models import Review
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Avg



class ReviewsListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ReviewsSerializer



class ReviewsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ReviewsSerializer
    


