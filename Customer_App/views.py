from django.shortcuts import render
from Customer_App.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Customer_App.models import Customer

# Create your views here.

@api_view(["GET", "POST", "PATCH"])
def customer_view(request, id=None):

    if request.method == "GET":
        if id is None:
            customers = Customer.objects.all().order_by('-id')
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)


    if request.method == "POST":
        print(request.data)
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer Created Successfully"}, status=201)
        
        return Response(serializer.errors, status=501)
    

    if request.method == "PATCH":
        if id:
            customer = Customer.objects.get(pk=id)
        else:
            customer = Customer.objects.get(pk=request.data["id"])

        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({"message": "Customer Updated Successfully"}, status=201)

        return Response(serializer.errors, status=501)