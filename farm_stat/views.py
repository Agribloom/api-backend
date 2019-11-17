from rest_framework import generics
from farm_stat.models import Testimony, Achievement, Partner
from farm_stat.serializers import TestimonySerializer, AchievementSerializer, PartnerSerializer


class TestimonyList(generics.ListAPIView):

    serializer_class = TestimonySerializer
    filterset_fields = ['created', 'updated']

    def get_queryset(self):
        return Testimony.objects.all()


class AchievementList(generics.ListAPIView):

    serializer_class = AchievementSerializer

    def get_queryset(self):
        return Achievement.objects.all()


class PartnerList(generics.ListAPIView):

    serializer_class = PartnerSerializer

    def get_queryset(self):
        return Partner.objects.all()
