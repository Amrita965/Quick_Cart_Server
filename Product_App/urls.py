
from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path("products/<int:pk>", product_detail),
    path("products", product_list),
    path("products/<str:pk>", product_list),

]
