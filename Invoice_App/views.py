from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InvoiceSerializer, InvoiceProductSerializer
from rest_framework import status

# Create your views here.

@api_view(["GET", "POST"])
def invoice_list(request):

    if request.method == "POST":
        bill = request.data["bill"]
        invoice_products = request.data["invoice_products"]
        serializer = InvoiceSerializer(data=bill)
        if serializer.is_valid():
            invoice = serializer.save()
            
            for invoice_product in invoice_products:
                product = {
                    "invoice": invoice.id,
                    "product": invoice_product["id"],
                    "user": bill["user"],
                    "quantity": invoice_product["quantity"],
                    "sale_price": invoice_product["total_price"]
                }
                serializer = InvoiceProductSerializer(data=product)
                if serializer.is_valid():
                    serializer.save()

                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

            return Response({"message": "The order has been successfully confirmed."})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        