from django.urls import path
from crowdfund.views import FarmListAPIView, FarmDetailView, CategoryListAPIView

urlpatterns = [
    path('farms', FarmListAPIView.as_view(), name='farm_list'),
    path("farms/<int:pk>", FarmDetailView.as_view(), name='farm_detail'),
    path('categories', CategoryListAPIView.as_view(), name='category'),
]
