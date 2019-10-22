from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_auth.serializers import UserDetailsSerializer
from accounts.models import Transaction

UserModel = get_user_model()

class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta:
        model = UserModel
        fields = (
            'pk', 'username', 'first_name', 'last_name',
            'email', 'address', 'phone_number', 'date_of_birth', 'gender',
            'bank_name', 'account_name', 'account_number'
        )
        read_only_fields = ('email', 'username')


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = (
            '__all__'
        )

        read_only_fields = (
            'owner',
        )
    