from rest_framework.serializers import ModelSerializer, ReadOnlyField, HyperlinkedModelSerializer
from crowdfund.models import Category, Farm, FarmManager, Update, UpdateImage


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )


class UpdateImageSerializer(ModelSerializer):

    class Meta:
        model = UpdateImage
        fields = (
            'id', 'image', 'position'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )


class UpdateSerializer(ModelSerializer):

    images = UpdateImageSerializer(source='updateimage_set', many=True, read_only=True)

    class Meta:
        model = Update
        fields = (
            "id", "activity", "slug", "description",
            "report", "images", "date", "created", "updated",
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )


class FarmSerializer(ModelSerializer):

    updates = UpdateSerializer(source='update_set', many=True, read_only=True)

    class Meta:
        model = Farm
        fields = (
            "id", "name", "slug", "description", "status", "duration",
            "location", "insurance_statement", "insured", "units",
            "unit_in_stock", "price_per_unit_currency", "price_per_unit",
            "roi", "image", "stage", "harvest_date", "start_date",
            "end_date", "manger", "category", "updates", "created", "updated"
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
