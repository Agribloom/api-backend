from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_auth.serializers import UserDetailsSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from allauth.account.forms import default_token_generator
from allauth.account.utils import url_str_to_user_pk
from accounts.forms import CustomRestResetPasswordForm
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
    password_reset_form_class = CustomRestResetPasswordForm


class CustomPasswordResetConfirmSerializer(PasswordResetConfirmSerializer):
    """
    Serializer for requesting a password reset e-mail.
    """

    def validate(self, attrs):
        self._errors = {}

        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(url_str_to_user_pk(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        return attrs

    def save(self):
        return self.set_password_form.save()