from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('standard', 'Standard'),
        ('pro', 'Pro'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')

    def __str__(self):
        return f"{self.user.username} - {self.plan_type}"