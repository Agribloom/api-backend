from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_auth.serializers import UserDetailsSerializer
from rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm 
from accounts.models import Transaction
from crowdfund.serializers import FarmMetaSerializer

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

    farm = FarmMetaSerializer()

    class Meta:
        model = Transaction
        fields = (
            'farm', 'description', 'status', 'transaction_type',
            'amount', 'amount_currency', 'created', 'updated'
        )

        # read_only_fields = (
        #     'owner',
        # )

class PasswordSerializer(PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm