from rest_framework import serializers
from .models import SwotModel, UserProfile

class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = SwotModel
        exclude = ['author', 'author_role']

# class UserProfileSerializer(serializers.ModelSerializer):
#     first_name = serializers.CharField(source='user.first_name', required=True)
#     last_name = serializers.CharField(source='user.last_name', required=True)
#     email = serializers.CharField(source='user.email', required=True)
#
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

