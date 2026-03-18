from django.shortcuts import render
from rest_framework import APIView #APIView is imported for creating class-based views
from rest_framework.response import Response #Response is imported for sending responses back to the client
from .serializers import RegisterSerializer, LoginSerializer #RegisterSerializer and LoginSerializer are imported for handling user registration and login
from rest_framework import status #status is imported for sending appropriate HTTP status codes in responses
from django.contrib.auth import login, logout #login and logout are imported for handling user authentication

# Create your views here.
class RegisterView(APIView):#RegisterView is a class-based view that handles user registration
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)#The post method is defined to handle POST requests for user registration. It takes the request data and passes it to the RegisterSerializer for validation and saving.
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):#LoginView is a class-based view that handles user login
    def post(self, request):
        serializer = LoginSerializer(data=request.data)#The post method is defined to handle POST requests for user login. It takes the request data and passes it to the LoginSerializer for validation.
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)#If the serializer is valid, the user is authenticated and logged in using Django's built-in login function.
            return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):#LogoutView is a class-based view that handles user logout
    def post(self, request):
        logout(request)#The post method is defined to handle POST requests for user logout. It uses Django's built-in logout function to log the user out.
        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)