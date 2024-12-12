
from django.urls import path
from Customer_App.views import customer_view

urlpatterns = [
    path('customers/', customer_view),
    path('customers/<int:id>', customer_view)
]
