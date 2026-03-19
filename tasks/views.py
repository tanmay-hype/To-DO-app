from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer

#generics is imported for creating generic class-based views
#permissions is imported for handling permissions and access control
#Task is imported for querying the Task model and performing CRUD operations
#TaskSerializer is imported for serializing and deserializing Task instances



# Create your views here.

class TaskListCreateView(generics.ListCreateAPIView):#TaskListCreateView is a class-based view that handles listing and creating tasks
    #queryset = Task.objects.all()#The queryset attribute is defined to specify the set of data that will be used for this view. In this case, it retrieves all Task objects from the database.
    serializer_class = TaskSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the TaskSerializer to serialize and deserialize Task instances.
    permission_classes = [permissions.IsAuthenticated]#The permission_classes attribute is defined to specify the permissions required to access this view. In this case, it requires the user to be authenticated to access the view.
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)
    
   # def perform_create(self, serializer):
       # serializer.save(user=self.request.user)#The perform_create method is overridden to associate the created task with the authenticated user. When a new task is created, it automatically sets the user field of the task to the currently authenticated user, ensuring that tasks are linked to the correct user in the database.


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):#TaskDetailView is a class-based view that handles retrieving, updating, and deleting individual tasks
    #queryset = Task.objects.all()#The queryset attribute is defined to specify the set of data that will be used for this view. In this case, it retrieves all Task objects from the database.
    serializer_class = TaskSerializer#The serializer_class attribute is defined to specify the serializer that will be used for this view. In this case, it uses the TaskSerializer to serialize and deserialize Task instances.
    permission_classes = [permissions.IsAuthenticated]#The permission_classes attribute is defined to specify the permissions required to access this view. In this case, it requires the user to be authenticated to access the view.

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)#The get_queryset method is overridden to filter the queryset based on the authenticated user. It retrieves only the tasks that belong to the currently authenticated user, ensuring that users can only access their own tasks.
    