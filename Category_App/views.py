# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework import status
from User_App.models import User
from Category_App.models import Category
from django.db.models import Q

# Create your views here.

@api_view(["GET", "POST"])
def category_list(request, pk=None):

    if request.method == "GET":
        if pk is not None:
            user = User.objects.get(pk=pk)
            searchText = request.GET.get("searchText", "")
            page = int(request.GET.get("page"))
            limit = int(request.GET.get("limit"))
            
            total = Category.objects.count()

            if searchText:
                if searchText.isdigit():
                    categories = user.categories.filter(id=searchText)
                else:
                    categories = user.categories.filter(Q(
                        name__icontains = searchText
                    ))
            else:
                categories = user.categories.all().order_by("-id")[(page -1) * limit: page * limit]

            serializer = CategorySerializer(categories, many=True)
            return Response({
                "total": total,
                "categories": serializer.data
            })

    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PATCH", "DELETE"])
def category_detail(request, pk):

    try:
        category = Category.objects.get(pk=pk)
    except Exception as _:
        return Response({"message": "Category doesn't exist"})
    
    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        print(request.data)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Category Updated Successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to update category"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        category.delete()
        return Response({"message": "Category Deleted Sucessfully"}, status=status.HTTP_200_OK)
