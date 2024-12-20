from django.db import models
from User_App.models import User
from Customer_App.models import Customer
from Product_App.models import Product

# Create your models here.

class Invoice(models.Model):

    total = models.FloatField()
    discount = models.FloatField()
    vat = models.FloatField()
    payable = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="invoices")
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name="invoices")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     pass

    class Meta:
        db_table = "invoices"

class InvoiceProduct(models.Model):

    invoice = models.ForeignKey(Invoice, on_delete=models.RESTRICT, related_name="invoice_products")
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    quantity = models.IntegerField()
    sale_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "invoice_products"