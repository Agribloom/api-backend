from rest_framework import serializers
from farm_stat.models import Testimony, Achievement, Partner


class TestimonySerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimony
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #
