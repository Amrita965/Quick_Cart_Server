from django.db import models
from User_App.models import User

# Create your models here.

class Category(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return f"Category Name: {self.name}"