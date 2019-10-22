from django.urls import path
from crowdfund.views import FarmListAPIView, ProjectListAPIView, CategoryListAPIView

urlpatterns = [
    path('farms', FarmListAPIView.as_view(), name='farms'),
    path('projects', ProjectListAPIView.as_view(), name='projects'),
    path('categories', CategoryListAPIView.as_view(), name='category'),
]
