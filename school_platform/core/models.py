from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('schooladmin', 'School Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
