
from django.urls import path
from .views import category_list, category_detail

urlpatterns = [
    path('categories/<int:pk>', category_detail),
    path('categories', category_list),
    path('categories/<str:pk>', category_list),

]
