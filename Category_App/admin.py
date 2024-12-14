from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "user", "created_at", "updated_at")
    search_fields = ("id", "name")