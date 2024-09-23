from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user__username']


@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ['cart__user__username','product__name', 'quantity']