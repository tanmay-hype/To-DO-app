from django.shortcuts import render
from rest_framework.views import APIView #APIView is imported for creating class-based views
from rest_framework.response import Response #Response is imported for sending responses back to the client
from .serializers import RegisterSerializer, LoginSerializer #RegisterSerializer and LoginSerializer are imported for handling user registration and login
from rest_framework import status #status is imported for sending appropriate HTTP status codes in responses
from rest_framework.authentication import SessionAuthentication #SessionAuthentication is imported for handling session-based authentication
from rest_framework import generics, permissions #generics and permissions are imported for handling permissions and access control
from .serializers import UserSerializer #UserSerializer is imported for serializing user data
from .models import User #User is imported for querying the User model and performing CRUD operations
from .permissions import IsOwner #IsOwner is imported for handling object-level permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt_serializer import CustomTokenSerializer #CustomTokenSerializer is imported for customizing the JWT token generation process   




class CsrExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening in SessionAuthentication


# Create your views here.
class RegisterView(APIView):#RegisterView is a class-based view that handles user registration
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)#The post method is defined to handle POST requests for user registration. It takes the request data and passes it to the RegisterSerializer for validation and saving.
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#class LoginView(APIView):#LoginView is a class-based view that handles user login
    #def post(self, request):
        #serializer = LoginSerializer(data=request.data)#The post method is defined to handle POST requests for user login. It takes the request data and passes it to the LoginSerializer for validation.
      #  if serializer.is_valid():
        #    user = serializer.validated_data
      #      login(request, user)#If the serializer is valid, the user is authenticated and logged in using Django's built-in login function.
      #      return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class LogoutView(APIView):#LogoutView is a class-based view that handles user logout
    #authentication_classes = [CsrExemptSessionAuthentication]
    
   # def post(self, request):
        #logout(request)#The post method is defined to handle POST requests for user logout. It uses Django's built-in logout function to log the user out.
        #return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)

class UserListCreateView(generics.ListCreateAPIView):#UserListView is a class-based view that handles listing and creating users
    queryset = User.objects.all()#The queryset attribute is defined to specify the set of data that will be used for this view. In this case, it retrieves all User objects from the database.
    serializer_class = UserSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the UserSerializer to serialize and deserialize User instances.
    permission_classes = [permissions.IsAuthenticated]#The permission_classes attribute is defined to specify the permissions required to access this view. In this case, it requires the user to be authenticated to access the view.


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):#UserDetailView is a class-based view that handles retrieving, updating, and deleting individual users
    queryset = User.objects.all()#The queryset attribute is defined to specify the set of data that will be used for this view. In this case, it retrieves all User objects from the database.
    serializer_class = UserSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the UserSerializer to serialize and deserialize User instances.
    permission_classes = [permissions.IsAuthenticated, IsOwner]#The permission_classes attribute is defined to specify the permissions required to access this view. In this case, it requires the user to be authenticated to access the view.  


class CustomTokenView(TokenObtainPairView):#CustomTokenView is a class-based view that handles JWT token generation using the CustomTokenSerializer
    serializer_class = CustomTokenSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the CustomTokenSerializer to generate JWT tokens with custom claims.