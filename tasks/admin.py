from django.contrib import admin
from .models import Category, Task

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')#The list_display attribute is defined to specify the fields that will be displayed in the admin list view for the Category model. In this case, it displays the id, name,and user fields of the Category model.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'category', 'user')#The list_display attribute is defined to specify the fields that will be displayed in the admin list view for the Task model. In this case, it displays the id, title, description, completed, category, and user fields of the Task model.
