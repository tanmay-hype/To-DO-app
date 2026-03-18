from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your custom user model by extending AbstractUser

class User(AbstractUser):
    # Add any additional fields you need for your custom user model
    pass


