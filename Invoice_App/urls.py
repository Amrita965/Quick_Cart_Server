
from django.urls import path
from .views import invoice_list, get_invoice_products

urlpatterns = [
    path("invoices/", invoice_list),
    path("invoices/<str:pk>/", invoice_list),
    path("invoice-products/<int:pk>", get_invoice_products)
]
