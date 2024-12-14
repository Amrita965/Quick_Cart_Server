
from django.urls import path
from Customer_App.views import customer_list, customer_detail
urlpatterns = [
    path('customers/<int:pk>', customer_detail),
    path('customers/', customer_list),
    path('customers/<str:uid>', customer_list),
]
