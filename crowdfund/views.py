from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from crowdfund.models import Category, Farm, FarmManager, Update, Investment
from crowdfund.serializers import CategorySerializer, FarmDetailSerializer, \
    FarmListSerializer, FarmManagerSerializer, UpdateSerializer, InvestmentSerializer


class FarmListAPIView(ListAPIView):

    serializer_class = FarmListSerializer
    filterset_fields = ['insured', 'status', 'category']

    def get_queryset(self):
        return Farm.objects.all()


class FarmDetailView(RetrieveAPIView):

    serializer_class = FarmDetailSerializer

    def get_queryset(self):
        return Farm.objects.all()


class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailView(RetrieveAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Farm.objects.all()


class CategoryDetailView(RetrieveAPIView):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Farm.objects.all()


class InvestmentListView(ListCreateAPIView):

    serializer_class = InvestmentSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Investment.objects.filter(
                owner=self.request.user
            )
        return Investment.objects.none()

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except Exception:
            raise serializers.ValidationError("Please login")
