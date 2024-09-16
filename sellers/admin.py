from django.contrib import admin
from .models import Seller



@admin.register(Seller)
class SellersModelAdmin(admin.ModelAdmin):
    list_display = [
        'enterprise_name',
        'name_fantasy',
        'email',
        'cnpj',
        'address',
        'address_number'
    ]
