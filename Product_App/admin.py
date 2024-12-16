from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "price", "unit", "img_url", "user_id", "category_id", "created_at", "updated_at")
    search_fields = ("id", "name")