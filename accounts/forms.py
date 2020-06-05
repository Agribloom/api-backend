from django.contrib.sites.shortcuts import get_current_site
from django.core import exceptions, validators
from django.urls import reverse
from django.utils.http import urlencode
from django import forms
from allauth.account.adapter import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import user_pk_to_url_str, user_username
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm, AddEmailForm, default_token_generator, build_absolute_uri
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    CustomUserCreationForm will be used from django admin site
    and is only available to staff users during user creation
    """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    """
    CustomUserChangeForm will be used from django admin site
    and is only available to staff users during user update
    """
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number',
                  'date_of_birth', 'bank_name', 'account_name', 'account_number')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'autofill': False
                }
            )
        }


class CustomRestResetPasswordForm(ResetPasswordForm):

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get("token_generator",
                                     default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            # path = reverse("account_reset_password_from_key",
            #                kwargs=dict(uidb36=user_pk_to_url_str(user),
            #                            key=temp_key))

            path = 'https://agribloom.farm/password/reset?key={0}-{1}'.format( # TODO: look for a dynamic alternative
                user_pk_to_url_str(user),
                temp_key
            )
            url = build_absolute_uri(
                request, path
            )

            context = {"current_site": current_site,
                       "user": user,
                       "password_reset_url": url,
                       "request": request}

            # if app_settings.AUTHENTICATION_METHOD \
            #         != AuthenticationMethod.EMAIL:
            #     context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/password_reset_key',
                email,
                context)
        return self.cleaned_data["email"]
