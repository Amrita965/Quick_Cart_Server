from django.contrib import admin
from Customer_App.models import Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "mobile", "user", "created_at", "updated_at")
    search_fields = ("name", "email", "mobile")
