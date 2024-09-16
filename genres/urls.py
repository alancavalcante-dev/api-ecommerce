from django.urls import path
from .views import (
    GenresListCreateAPIView,
    GenresRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('genres/', GenresListCreateAPIView.as_view(), name='detail-create-genres'),
    path('genres/<int:pk>/', GenresRetrieveUpdateDestroyAPIView.as_view(), name='update-delete-genres')
]
