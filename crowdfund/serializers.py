from rest_framework.serializers import ModelSerializer, ReadOnlyField, HyperlinkedModelSerializer
from crowdfund.models import Category, Project, Farm, PManager, Update


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'creator',
        # )


class FarmSerializer(ModelSerializer):

    class Meta:
        model = Farm
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )

class ProjectManagerSerializer(ModelSerializer):

    class Meta:
        model = PManager
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )

class UpdateSerializer(ModelSerializer):

    class Meta:
        model = Update
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )