
from django.urls import path
from .views import product_list

urlpatterns = [
    path("products/<str:pk>", product_list)
]
