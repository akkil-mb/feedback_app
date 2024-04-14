from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

class SwotModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    author_role = models.IntegerField(editable=False)
    full_name = models.CharField(max_length=100, default='')
    team_name = models.CharField(max_length=150, default='')
    designation = models.CharField(max_length=150, default='')
    joined_on = models.DateField(auto_now=timezone.now().date())

    strengths = models.CharField(max_length=1000)
    weakness = models.CharField(max_length=1000)
    opportunity = models.CharField(max_length=1000)
    threats = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.full_name)

ROLES = [
    (6, 'Team'),
    (5, 'Team Lead'),
    (4, 'Manager'),
    (3, 'HR'),
    (2, 'CEO'),
    (1, 'Super User'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField( choices=ROLES)


class DataEntryPermission(models.Model):
    role = models.IntegerField(choices=ROLES)
    can_post = models.BooleanField(default=True)
    can_view_role_1 = models.BooleanField(default=False)
    can_view_role_2 = models.BooleanField(default=False)
    can_view_role_3 = models.BooleanField(default=False)
    can_view_role_4 = models.BooleanField(default=False)

    def __str__(self):
        return f'Permission for role {self.role}'






