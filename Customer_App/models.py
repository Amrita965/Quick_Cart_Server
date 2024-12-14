from django.db import models
from User_App.models import User

# Create your models here.

class Customer(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return f"Customer Email: {self.email}"




