from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField


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


class Transaction(models.Model):

    PAID = 'paid'
    PENDING = 'pending'
    DEPOSIT = 'deposit'
    WITHDRAWAL = 'withdrawal'

    TRANSACTION_STATUS = (
        (PAID, 'Paid'),
        (PENDING, 'Pending'),
    )
    TRANSACTION_TYPE = (
        (DEPOSIT, 'Deposit'),
        (WITHDRAWAL, 'Withdrawal')
    )

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='NGN')
    status = models.CharField(max_length=50, choices=TRANSACTION_STATUS)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "transaction"
        verbose_name_plural = "transactions"

    def __str__(self):
        return self.owner.get_username_or_fullname()

    def get_absolute_url(self):
        return reverse("transaction_detail", kwargs={"pk": self.pk})
