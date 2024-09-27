from django.urls import path
from .views import (
    ReviewsListCreateAPIView,
    ReviewsRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('reviews/', ReviewsListCreateAPIView.as_view(), name='detail-create-reviews'),
    path('reviews/<int:pk>/', ReviewsRetrieveUpdateDestroyAPIView.as_view(), name='update-delete-reviews'),
]
