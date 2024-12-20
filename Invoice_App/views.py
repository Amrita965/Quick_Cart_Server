from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .serializers import InvoiceSerializer, InvoiceProductSerializer, InvoiceCreateSerializer, InvoiceProductCreateSerializer
from User_App.models import User
from Invoice_App.models import Invoice

@api_view(["GET", "POST"])
def invoice_list(request, pk=None):

    if pk is not None:
        try:
            # Safely get the user by pk
            user = User.objects.get(pk=pk)
            # Fetch invoices related to the user and pre-fetch related customers
            # print(user.invoices.all())
            invoices = user.invoices.all().order_by("-id")
            # print(invoices)
            
            # Count total number of invoices for the user
            total = invoices.count()  # Using the same queryset for counting
            
            # Serialize the invoices
            serializer = InvoiceSerializer(invoices, many=True)

            return Response({
                "total": total,
                "invoices": serializer.data
            })

        except User.DoesNotExist:
            # Return an error response if the user doesn't exist
            return Response({"error": "User not found"}, status=404)


    if request.method == "POST":
        bill = request.data.get("bill", {})  # Safely get 'bill'
        invoice_products = request.data.get("invoice_products", [])  # Safely get 'invoice_products'

        try:
            with transaction.atomic():  # Ensure all operations are done atomically
                # Save the invoice
                invoice_serializer = InvoiceCreateSerializer(data=bill)
                if not invoice_serializer.is_valid():
                    return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                invoice = invoice_serializer.save()

                # Save each invoice product
                for invoice_product in invoice_products:
                    product_data = {
                        "invoice": invoice.id,
                        "product": invoice_product["id"],
                        "user": bill["user"],
                        "quantity": invoice_product["quantity"],
                        "sale_price": invoice_product["total_price"]
                    }
                    product_serializer = InvoiceProductCreateSerializer(data=product_data)
                    if not product_serializer.is_valid():
                        raise ValueError(product_serializer.errors)  # Raise error to trigger rollback
                    product_serializer.save()

                # If everything succeeds
                return Response({"message": "The order has been successfully confirmed."}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Handle GET request (if applicable)
    return Response({"message": "GET method not implemented yet."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET"])
def get_invoice_products(request, pk):
    if request.method == "GET":
        invoice = Invoice.objects.get(pk=pk)
        invoice_products = invoice.invoice_products.all()
        serializer = InvoiceProductSerializer(invoice_products, many=True)
        
        return Response(serializer.data)

