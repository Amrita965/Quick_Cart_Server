from django.shortcuts import render
from Customer_App.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Customer_App.models import Customer
from User_App.models import User
from rest_framework import status
from django.db.models import Q

# Create your views here.

@api_view(["GET", "POST"])
def customer_list(request, uid=None):

    if request.method == "GET":
        if id:
            print(type(request.GET.get('page')))
            page = int(request.GET.get('page'))
            limit = int(request.GET.get('limit'))
            search_text = request.GET.get('search', '')

            print(search_text)
        
            user = User.objects.get(pk=uid)
            # total_objects = MyModel.objects.count()
            total_customer = Customer.objects.count()

            if search_text:
                if search_text.isdigit():
                    customers = user.customers.filter(
                         Q(id=search_text) |
                         Q(mobile__icontains=search_text)
                    )

                else:
                    customers = user.customers.filter(
                        Q(name__icontains=search_text) |
                        Q(email__icontains=search_text) 
                    )
        
            else:
                customers = user.customers.all()[(page - 1) * limit : (page * limit)]
            
            serializer = CustomerSerializer(customers, many=True)
            return Response({"total": total_customer, "customers":serializer.data})

    if request.method == "POST":
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET", "PATCH", "DELETE"])
def customer_detail(request, pk):

    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    if request.method == "PATCH":

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "Customer Updated Successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=501)
    
    if request.method == "DELETE":
        customer.delete()
        return Response({"message": "Customer Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)