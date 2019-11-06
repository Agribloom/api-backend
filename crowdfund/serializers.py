from rest_framework.serializers import ModelSerializer, ReadOnlyField, HyperlinkedModelSerializer
from crowdfund.models import Category, Farm, FarmManager, Update


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'name', 'description'
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

class FarmManagerSerializer(ModelSerializer):

    class Meta:
        model = FarmManager
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