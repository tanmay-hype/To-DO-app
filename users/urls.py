from django.urls import path
from .views import RegisterView, LoginView, LogoutView , UserListCreateView, UserDetailView #RegisterView, LoginView and LogoutView are imported from the views module to be used in the URL patterns
#RegisterView, LoginView and LogoutView are imported 
# from the views module to be used in the URL patterns

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),#The URL pattern for user registration is defined, which maps to the RegisterView class-based view.
    path('login/', LoginView.as_view(), name='login'),#The URL pattern for user login is defined, which maps to the LoginView class-based view.
    path('logout/', LogoutView.as_view(), name='logout'),#The URL pattern for user logout is defined, which maps to the LogoutView class-based view.
    path('', UserListCreateView.as_view(), name='user-list-create'),#The URL pattern for listing and creating users is defined, which maps to the UserListCreateView class-based view.
    path('/<int:pk>/', UserDetailView.as_view(), name='user-detail'),#The URL pattern for user detail view is defined, which includes a dynamic segment <int:pk> to capture the primary key of the user. This allows for retrieving, updating, or deleting a specific user based on its unique identifier.]
]