
from rest_framework import serializers
from .models import Invoice, InvoiceProduct
from Customer_App.serializers import CustomerSerializer
from Product_App.serializers import ProductSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer() 

    class Meta:
        model = Invoice
        fields = "__all__"

class InvoiceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"

class InvoiceProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    class Meta:
        model = InvoiceProduct
        fields = "__all__"


class InvoiceProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceProduct
        fields = "__all__"
