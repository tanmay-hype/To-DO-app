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
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin, IsOwnerOrReadOnly #IsAdminOrReadOnly and IsOwnerOrReadOnly are imported for handling object-level permissions based on user roles and ownership
from django.contrib.auth.tokens import default_token_generator #default_token_generator is imported for generating tokens for password reset and account activation
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode #urlsafe_base64_encode and urlsafe_base64_decode are imported for encoding and decoding user IDs in a URL-safe format, typically used in password reset and account activation links
from django.utils.encoding import force_bytes, force_str #force_bytes and force_str are imported for
from django.core.mail import send_mail #send_mail is imported for sending emails, such as password reset emails or account activation emails
from django.conf import settings #settings is imported for accessing project settings, such as email configuration for sending emails
from django.contrib.auth import get_user_model




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
    


class UserListCreateView(generics.ListCreateAPIView):#UserListView is a class-based view that handles listing and creating users
    queryset = User.objects.all()#The queryset attribute is defined to specify the set of data that will be used for this view. In this case, it retrieves all User objects from the database.
    serializer_class = UserSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the UserSerializer to serialize and deserialize User instances.
    permission_classes = [IsAdminOrReadOnly]#The permission_classes attribute is defined to specify the permissions required to access this view. In this case, it requires the user to be authenticated to access the view.


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):#UserDetailView is a class-based view that handles retrieving, updating, and deleting individual users
    queryset = User.objects.all()#The queryset attribute is defined to specify the set of data that will be used for this view. In this case, it retrieves all User objects from the database.
    serializer_class = UserSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the UserSerializer to serialize and deserialize User instances.
    permission_classes = [ permissions.IsAuthenticated, IsOwnerOrAdmin]#The permission_classes attribute is defined to specify the permissions required to access this view. In this case, it requires the user to be authenticated to access the view.  


class CustomTokenView(TokenObtainPairView):#CustomTokenView is a class-based view that handles JWT token generation using the CustomTokenSerializer
    serializer_class = CustomTokenSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the CustomTokenSerializer to generate JWT tokens with custom claims.


User = get_user_model() 

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response({"error": "Email is required"}, status=400)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        reset_link = f"http://127.0.0.1:8000/users/reset-password/{uid}/{token}/"

        send_mail(
            subject="Password Reset",
            message=f"Click the link:{reset_link}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        # ✅ VERY IMPORTANT
        return Response({"message": "Password reset link sent"}, status=200)        
    
class ResetPasswordView(APIView):#ResetPasswordView is a class-based view that handles the password reset process when a user clicks on the password reset link sent to their email
    def post(self, request, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))#The post method is defined to handle POST requests for resetting the password. It takes the encoded user ID (uidb64) and the token from the URL parameters. The encoded user ID is decoded using urlsafe_base64_decode and force_str to retrieve the original user ID.
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({"error": "Invalid reset link"}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):#The token is validated using the default_token_generator's check_token method to ensure that it is valid and has not expired.
            new_password = request.data.get('new_password')#If the token is valid, the new password is retrieved from the request data and set for the user. The user's password is updated in the database, and a success response is returned.
            user.set_password(new_password)
            user.save()
            return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)