from django.db import models

# Create your models here.

class User(models.Model):
    
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    photo_URL = models.URLField()
    role = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="users"

    def __str__(self):
        return f"Email: {self.email}"