from rest_framework.serializers import ModelSerializer, ReadOnlyField, HyperlinkedModelSerializer
from crowdfund.models import Category, Farm, FarmManager, Update, UpdateImage, Investment


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

    images = UpdateImageSerializer(
        source='updateimage_set', many=True, read_only=True)

    class Meta:
        model = Update
        fields = (
            "id", "activity", "slug", "description",
            "report", "images", "date", "created", "updated",
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )


class FarmDetailSerializer(ModelSerializer):

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


class FarmListSerializer(ModelSerializer):

    class Meta:
        model = Farm
        fields = (
            "id", "name", "slug", "description", "status", "duration",
            "location", "insurance_statement", "insured", "units",
            "unit_in_stock", "price_per_unit_currency", "price_per_unit",
            "roi", "image", "stage", "harvest_date", "start_date",
            "end_date", "manger", "category", "created", "updated"
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


class FarmMetaSerializer(ModelSerializer):

    class Meta:
        model = Farm
        fields = (
            "id", "name", "slug", "status", "location", "units",
            "unit_in_stock", "price_per_unit_currency", "price_per_unit",
            "roi",
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )


class InvestmentSerializer(ModelSerializer):

    farm = FarmMetaSerializer()

    class Meta:
        model = Investment
        fields = (
            'farm', 'amount', 'units', 'amount',
            'amount_currency', 'created', 'updated'
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )
