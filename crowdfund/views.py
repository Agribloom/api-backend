from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from crowdfund.models import Category, Farm, FarmManager, Update
from crowdfund.serializers import CategorySerializer, FarmSerializer, FarmManagerSerializer, UpdateSerializer

class FarmListAPIView(ListAPIView):
    
    serializer_class = FarmSerializer
    filterset_fields = ['insured', 'status', 'category']
    
    
    def get_queryset(self):
        return Farm.objects.all()



class CategoryListAPIView(ListAPIView):
    
    serializer_class = CategorySerializer
    
    
    def get_queryset(self):
        return Category.objects.all()
