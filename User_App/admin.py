from django.contrib import admin
from User_App.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "photo_URL", "role", "created_at", "updated_at")
    search_fields = ("id", "name", "email", "role")
