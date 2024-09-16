from django.contrib import admin
from .models import Review

# Register your models here.
@admin.register(Review)
class ReviewsModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product','rate', 'date']
    