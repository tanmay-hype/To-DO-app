from django.urls import path
from .views import RegisterView, LoginView, LogoutView 
#RegisterView, LoginView and LogoutView are imported 
# from the views module to be used in the URL patterns

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),#The URL pattern for user registration is defined, which maps to the RegisterView class-based view.
    path('login/', LoginView.as_view(), name='login'),#The URL pattern for user login is defined, which maps to the LoginView class-based view.
    path('logout/', LogoutView.as_view(), name='logout'),#The URL pattern for user logout is defined, which maps to the LogoutView class-based view.
]