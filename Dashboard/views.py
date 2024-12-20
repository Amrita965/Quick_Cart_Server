from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Customer_App.models import Customer
from Category_App.models import Category
from User_App.models import User
from rest_framework import status
from django.db.models import Sum


# Create your views here.

@api_view(["GET"])
def dashborad_status(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except Exception as _:
        return Response({"message:", "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    
    total_categories = user.categories.count()
    total_customers = user.customers.count()
    total_products = user.products.count()
    invoices = user.invoices.all()

    totals = invoices.aggregate(total_vat=Sum('vat'), total_sale=Sum('total'))
    total_vat = round(totals['total_vat'] or 0, 2)
    total_sale = round(totals['total_sale'] or 0, 2)
    total_collection = round(total_sale + total_vat, 2)

    data = {
        "total_categories": total_categories,
        "total_customers": total_customers,
        "total_products": total_products,
        "total_invoices": invoices.count(),
        "total_vat": total_vat,
        "total_sale": total_sale,
        "total_collection": total_collection,
    }
    
    return Response(data)