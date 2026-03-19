from django.urls import path
from .views import TaskListCreateView, TaskDetailView, CategoryListCreateView, CategoryDetailView   


urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),#The URL
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),#The URL pattern for task detail view is defined, which includes a dynamic segment <int:pk> to capture the primary key of the task. This allows for retrieving, updating, or deleting a specific task based on its unique identifier.


    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'), 
    
]

