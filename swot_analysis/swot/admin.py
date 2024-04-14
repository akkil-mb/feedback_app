from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import SwotModel, UserProfile

class SwotAdmin(admin.ModelAdmin):
    list_display = ['full_name','team_name', 'designation', 'joined_on']

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline,]

admin.site.register(SwotModel, SwotAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)