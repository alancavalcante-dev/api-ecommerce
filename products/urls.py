from django.urls import path
from .views import (
    ProductsListCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('products/', ProductsListCreateAPIView.as_view(), name='detail-create-products'),
    path('products/<int:pk>/', ProductsRetrieveUpdateDestroyAPIView.as_view(), name='update-delete-products')
]
