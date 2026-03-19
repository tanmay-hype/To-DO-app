from django.db import models
from django.conf import settings


# 🔹 Category Model
class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    name = models.CharField(max_length=100)

    class Meta:
        # Prevent duplicate categories for same user
        unique_together = ['user', 'name']
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.user.username})"


# 🔹 Task Model
class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Latest tasks first
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['completed']),
        ]

    def __str__(self):
        return f"{self.title} ({self.user.username})"