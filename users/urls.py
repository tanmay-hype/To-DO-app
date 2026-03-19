from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView #TokenObtainPairView and TokenRefreshView are imported for handling JWT authentication
from .views import RegisterView, UserListCreateView, UserDetailView #RegisterView, LoginView and LogoutView are imported from the views module to be used in the URL patterns
from .views import ForgotPasswordView, ResetPasswordView
from .views import CustomTokenView #CustomTokenView is imported for handling JWT token generation with custom claims
#RegisterView, LoginView and LogoutView are imported 
# from the views module to be used in the URL patterns

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),#The URL pattern for user registration is defined, which maps to the RegisterView class-based view.
    path('token/', CustomTokenView.as_view(), name='custom_obtain_pair'),#The URL pattern for JWT token generation is defined, which maps to the CustomTokenView class-based view. This allows clients to obtain JWT tokens with custom claims when they log in.
   
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),#The URL pattern for initiating the password reset process is defined, which maps to the ForgotPasswordView class-based view. This allows users to request a password reset by providing their email address.
    path('reset-password/<uid>/<token>/', ResetPasswordView.as_view(), name='reset-password'),#The URL pattern for resetting the password is defined, which includes dynamic segments <uid> and <token> to capture the user ID and the password reset token. This allows users to reset their passwords by accessing this URL with the appropriate parameters.

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
    path('', UserListCreateView.as_view(), name='user-list-create'),#The URL pattern for listing and creating users is defined, which maps to the UserListCreateView class-based view.
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),#The URL pattern for user detail view is defined, which includes a dynamic segment <int:pk> to capture the primary key of the user. This allows for retrieving, updating, or deleting a specific user based on its unique identifier.]
]