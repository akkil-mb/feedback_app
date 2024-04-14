from django.urls import path, include
from .views import AnalysisListViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('data', AnalysisListViewset, basename='data')

urlpatterns = [
    path('', include(router.urls)),
]