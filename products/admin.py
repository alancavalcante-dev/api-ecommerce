from django.contrib import admin
from .models import Product



@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['seller__enterprise_name', 'genres__name','name', 'value','quantity']
