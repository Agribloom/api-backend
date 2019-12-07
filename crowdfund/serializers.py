import requests
from django.conf import settings
from requests.exceptions import HTTPError
from rest_framework import serializers
from agribloom.utils import PaystackAuth
from crowdfund.models import Category, Farm, FarmManager, Update, UpdateImage, Investment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )


class UpdateImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UpdateImage
        fields = (
            'id', 'image', 'position'
        )

        # read_only_fields = (
        #     'name', 'description'
        # )


class UpdateSerializer(serializers.ModelSerializer):

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


class FarmDetailSerializer(serializers.ModelSerializer):

    updates = UpdateSerializer(source='update_set', many=True, read_only=True)

    class Meta:
        model = Farm
        fields = (
            "id", "name", "slug", "description", "status", "duration",
            "location", "insurance_statement", "insured", "units",
            "unit_in_stock", "price_per_unit_currency", "price_per_unit",
            "raised", 'raised_currency', 'target', 'target_currency',
            "roi", "image", "stage", "harvest_date", "start_date",
            "end_date", "manger", "category", "updates", "created", "updated"
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )


class FarmListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = (
            "id", "name", "slug", "description", "status", "duration",
            "location", "insurance_statement", "insured", "units",
            "unit_in_stock", "price_per_unit_currency", "price_per_unit",
            "raised", 'raised_currency', 'target', 'target_currency',
            "roi", "image", "stage", "harvest_date", "start_date",
            "end_date", "manger", "category", "created", "updated"
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )


class FarmManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmManager
        fields = (
            '__all__'
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )


class FarmMetaSerializer(serializers.ModelSerializer):

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


class InvestmentSerializer(serializers.ModelSerializer):

    # farm = FarmMetaSerializer()

    def validate_transaction_id(self, value):
        url = 'https://api.paystack.co/transaction/verify/{}'.format(
            value
        )
        try:
            response = requests.get(
                url,
                auth=PaystackAuth(settings.PAYSTACK_SECRET_KEY)
            )
            json_response = response.json()
            # print(json_response)
            status = json_response.get('data').get('status')
            if status == 'success':
                return value
            else:
                raise serializers.ValidationError('Invalid transaction')

            raise serializers.ValidationError('Invalid transaction')
        except HTTPError as http_err:
            raise serializers.ValidationError(
                f'HTTP error occurred: {http_err.response.content}'
            )  # Python 3.6
        except Exception as err:
            raise serializers.ValidationError(
                f'Other error occurred: {err}'
            )  # Python 3.6
        else:
            raise serializers.ValidationError('value')

    class Meta:
        model = Investment
        fields = (
            'farm', 'amount', 'units', 'transaction_id',
            'amount_currency', 'created', 'updated',
        )

        # read_only_fields = (
        #     'expires', 'user'
        # )
