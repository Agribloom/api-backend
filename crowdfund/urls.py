from django.urls import path
from crowdfund.views import FarmListAPIView, CategoryListAPIView

urlpatterns = [
    path('farms', FarmListAPIView.as_view(), name='farms'),
    path('categories', CategoryListAPIView.as_view(), name='category'),
]
