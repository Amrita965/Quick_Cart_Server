from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Customer_App.models import Customer
from Category_App.models import Category
from User_App.models import User
from rest_framework import status


# Create your views here.

@api_view(["GET"])
def dashborad_status(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except Exception as _:
        return Response({"message:", "User doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    
    total_categories = len(user.categories.all())
    total_customers = len(user.customers.all())
    total_products = len(user.products.all())

    data = {
        "total_categories": total_categories,
        "total_customers": total_customers,
        "total_products": total_products
    }

    return Response(data)