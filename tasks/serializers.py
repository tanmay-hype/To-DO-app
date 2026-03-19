from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']
# The TaskSerializer is a ModelSerializer that automatically generates fields based on the Task model.
# The Meta class specifies the model to be serialized and the fields to include in the serialization.
# fields = '__all__' indicates that all fields of the Task model should be included in the serialization.

