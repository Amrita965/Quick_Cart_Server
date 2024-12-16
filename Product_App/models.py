from django.db import models
from User_App.models import User
from Category_App.models import Category

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.FloatField()
    unit = models.IntegerField()
    img_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product Name: {self.name}"

    class Meta:
        db_table = "Products"