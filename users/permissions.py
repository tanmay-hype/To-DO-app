from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
    
# The IsOwner class is a custom permission class that inherits from permissions.BasePermission. It defines the has_object_permission method, which checks if the user associated with the object (obj.user) is the same as the currently authenticated user (request.user). If they match, the permission is granted; otherwise, it is denied. This permission class can be used to restrict access to objects based on ownership, ensuring that users can only access their own data.