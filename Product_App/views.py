from django.shortcuts import render
from Product_App.models import Product
from User_App.models import User
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

# Create your views here.

@api_view(["GET", "POST"])
def product_list(request, pk=None):

    if pk is not None:

        user = User.objects.get(pk=pk)
        products = user.products.all().order_by("-id")
        total = Product.objects.count()

        serializer = ProductSerializer(products, many=True)

        return Response({
            "total": total,
            "products": serializer.data
        })

