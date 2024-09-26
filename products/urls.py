from django.urls import path
from .views import (
    ProductsListCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView,
    ProductsListAPIView,
    ProductsRetrieveAPIView,
    ProductsGenericView
    
)

urlpatterns = [
    path('products/', ProductsListAPIView.as_view(), name='detail-create-products'),
    path('products/<int:pk>/', ProductsRetrieveAPIView.as_view(), name='update-delete-products'),
    path('products/teste/', ProductsGenericView.as_view(), name='teste')
]
