from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          related_name='tasks') 
#The Task model has a foreign key relationship with the User model, which allows each task to be associated with a specific user.
# The on_delete=models.CASCADE argument ensures that if a user is deleted, all associated tasks will also be deleted.
   
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    #__str__ method is defined to return the title of the task when the object is printed or displayed in the admin interface.
