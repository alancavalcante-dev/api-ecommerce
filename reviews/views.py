from authentication.permission import GlobalPermissionClass
from .serializers import ReviewsSerializer
from .models import Review
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


class ReviewsListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ReviewsSerializer



class ReviewsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, GlobalPermissionClass,)
    serializer_class = ReviewsSerializer
    
    