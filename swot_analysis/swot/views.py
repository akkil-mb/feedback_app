from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import AnalysisSerializer
from .models import SwotModel
from .models import UserProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class AnalysisListViewset(viewsets.ModelViewSet):
    serializer_class = AnalysisSerializer
    queryset = SwotModel.objects.all()
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        current_user_id = request.user.id
        current_user = request.user
        if SwotModel.objects.filter(author_id=current_user_id).exists():
            return Response({'detail':'You have already submitted response'}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "POST":
            user_profile = UserProfile.objects.get(user=self.request.user)
            role_value = user_profile.role
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author_role=role_value, author=current_user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user=self.request.user)
        role_value = user_profile.role

        if role_value == 1:
            result = SwotModel.objects.all()
            return result
        elif role_value == 2:
            result = SwotModel.objects.filter(author_role__gte=role_value)
            return result
        else:
            result = SwotModel.objects.filter(author_role__gt=role_value)
            return result
