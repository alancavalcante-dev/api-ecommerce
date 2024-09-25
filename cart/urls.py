from django.urls import path
from .views import CartItemListAPIView, AddToCartView, QuantityCardItem, CartItemDestroyAPIView

urlpatterns = [
    path('cart/', CartItemListAPIView.as_view(), name='list'),
    path('cart/<int:pk>/', CartItemDestroyAPIView.as_view(), name='remove'),
    path('cart/add/', AddToCartView.as_view(), name='add'),
    path('cart/quantity-products/', QuantityCardItem.as_view(), name='quantity'),
]
