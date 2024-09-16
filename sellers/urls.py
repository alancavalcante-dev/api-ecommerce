from django.urls import path
from .views import (
    SellersListCreateAPIView,
    SellersRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('sellers/', SellersListCreateAPIView.as_view(), name='detail-create-sellers'),
    path('sellers/<int:pk>/', SellersRetrieveUpdateDestroyAPIView.as_view(), name='update-delete-sellers')
]
