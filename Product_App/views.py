from django.shortcuts import render
from Product_App.models import Product
from User_App.models import User
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from rest_framework import status
from django.db.models import Q

# Create your views here.

@api_view(["GET", "POST"])
def product_list(request, pk=None):

    if(request.method == "GET"): 
        if pk is not None:
            page = int(request.GET.get("page"))
            limit = int(request.GET.get("limit"))
            searchText = request.GET.get("searchText", "")

            print(request.GET)

            user = User.objects.get(pk=pk)

            if searchText:
                if searchText.isdigit():
                    products = user.products.filter(Q(id = searchText) | Q(price = searchText) | Q(unit = searchText))
                else:
                    products = user.products.filter(Q(name__icontains = searchText))
            else:
                products = user.products.all().order_by("-id")[(page - 1) * limit : (page * limit)]
            
            total = user.products.count()

            serializer = ProductSerializer(products, many=True)

            return Response({
                "total": total,
                "products": serializer.data
            })
    
    if request.method == "POST":

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message": "Product Created Successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors)


@api_view(["GET", "DELETE", "PATCH"])
def product_detail(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response({"message": "Product Doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        pass

    if request.method == "DELETE":
        product.delete()
        return Response({"message": "Product Deleted Successfully"})
    
    if request.method == "PATCH":
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product Updated Successfully"}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors)