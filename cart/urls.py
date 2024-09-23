from django.urls import path
from .views import CartItemListAPIView, AddToCartView

urlpatterns = [
    path('cart/', CartItemListAPIView.as_view(), name='list'),
    path('cart/add/', AddToCartView.as_view(), name='add'),

]
