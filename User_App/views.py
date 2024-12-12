# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from User_App.serializers import UserSerializer
# Create your views here.

@api_view(["GET", "POST", "PATCH"])
def user_view(request):

    if request.method == "GET":
        return Response({"message": "Hello World"})

    if request.method == "POST":
        print(request.POST)
        print(request.data)
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created Successfully"}, status=201)
        
        return Response(serializer.errors, status=501)




        