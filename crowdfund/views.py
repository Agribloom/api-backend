from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from crowdfund.models import Category, Farm, Project, PManager, Update
from crowdfund.serializers import CategorySerializer, FarmSerializer, ProjectManagerSerializer, UpdateSerializer, ProjectSerializer

class FarmListAPIView(ListAPIView):
    
    serializer_class = FarmSerializer
    filterset_fields = ['insured', 'status', 'category']
    
    
    def get_queryset(self):
        return Farm.objects.all()
    
    
class ProjectListAPIView(ListAPIView):
    
    serializer_class = ProjectSerializer
    filterset_fields = ['insured', 'status', 'catergory']
    
    
    def get_queryset(self):
        return Project.objects.all()

class CategoryListAPIView(ListAPIView):
    
    serializer_class = CategorySerializer
    
    
    def get_queryset(self):
        return Category.objects.all()
