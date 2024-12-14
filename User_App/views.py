# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from User_App.serializers import UserSerializer
from User_App.models import User
from rest_framework import status
# Create your views here.

@api_view(["GET", "POST"])
def user_list(request):

    if request.method == "POST":
        print(request.POST)
        print(request.data)
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created Successfully"}, status=201)
        
        return Response(serializer.errors, status=501)

@api_view(["GET", "PATCH", "DELETE"])
def user_detail(request, pk):

    print(pk)
    print(request.data)

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == "PATCH":
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User Updated Sucessfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

