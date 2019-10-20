from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):

    GENDERCHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = models.CharField(max_length=2, choices=GENDERCHOICES)
    date_of_birth = models.DateField("date of birth", null=True)
    phone_number = PhoneNumberField(verbose_name="phone number")
    # following = models.ManyToManyField("self", through='Peer', symmetrical=False, related_name='followers')
    address = models.CharField(max_length=255, null=True)

    # Account payment related details
    bank_name = models.CharField("bank name", max_length=255, null=True)
    account_name = models.CharField("account name", max_length=50, null=True)
    account_number = models.CharField("account number", max_length=11, null=True)

    def get_absolute_url(self):
        return reverse("user_profile", args=[self.username])

    def get_username_or_fullname(self):
        if not self.get_full_name().strip():
            return self.get_username()
        
        return self.get_full_name()

    def __str__(self):
        return self.get_username_or_fullname()