from .serializers import GenresSerializer
from .models import Genre
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


class GenresListCreateAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = GenresSerializer



class GenresRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = GenresSerializer
    
    