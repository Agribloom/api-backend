from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.conf import settings
from djmoney.models.fields import MoneyField


class FarmManager(models.Model):

    ROLE_TYPE = (
        ('Project Manager', 'Project Manager'),
        ('Farm Manager', 'Farm Manager')
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    farm = models.ForeignKey(
        "crowdfund.Farm", on_delete=models.CASCADE,
        null=True
    )
    role = models.CharField(max_length=50, choices=ROLE_TYPE)

    class Meta:
        verbose_name = "farm manager"
        verbose_name_plural = "farm managers"

    def __str__(self):
        return self.manager.get_username_or_fullname()

    def get_absolute_url(self):
        return reverse("manager_detail", kwargs={"pk": self.pk})


class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Farm(models.Model):

    PROJECT_OPEN = 'open'
    PROJECT_CLOSE = 'close'
    PROJECT_SOLD_OUT = 'sold_out'

    PROJECT_STATUS = (
        (PROJECT_OPEN, 'Open'),
        (PROJECT_CLOSE, 'Closed'),
        (PROJECT_SOLD_OUT, 'Sold out')
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=50, choices=PROJECT_STATUS,
        default=PROJECT_CLOSE
    )
    # manager = models.ForeignKey(
    #     FarmManager, verbose_name='farm manager',
    #     on_delete=models.CASCADE
    # )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=150)
    insurance_statement = models.TextField()
    insured = models.BooleanField(default=True)
    units = models.PositiveIntegerField()
    unit_in_stock = models.PositiveIntegerField()
    price_per_unit = MoneyField(
        max_digits=14, decimal_places=2,
        default_currency='NGN',
        default=0
    )
    roi = models.PositiveSmallIntegerField()
    raised = MoneyField(
        max_digits=14, decimal_places=2,
        default_currency='NGN',
        default=0
    )
    target = MoneyField(
        max_digits=14, decimal_places=2,
        default_currency='NGN'
    )
    image = models.ImageField(upload_to='images/farm/%Y/')
    stage = models.CharField('farm stage', max_length=50)
    harvest_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "farm"
        verbose_name_plural = "farms"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("farm_detail", kwargs={"slug": self.slug})


class Update(models.Model):

    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    report = models.TextField()
    date = models.DateField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Farm update"
        verbose_name_plural = "Farm updates"

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse("update_detail", kwargs={"slug": self.slug})


class UpdateImage(models.Model):

    update = models.ForeignKey(Update, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/farm/%Y')
    position = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Update Image"
        verbose_name_plural = "Update Images"

    def __str__(self):
        return '{} ({})'.format(self.update.farm.name, self.update.date)

    def get_absolute_url(self):
        return reverse("UpdateImage_detail", kwargs={"pk": self.pk})


class Investment(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    units = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)]
    )
    amount = MoneyField(
        max_digits=14, decimal_places=2,
        default_currency='NGN'
    )
    transaction_id = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    @property
    def full_name(self):
        return "%s %s"%(self.owner.first_name, self.owner.last_name)

    @property
    def bank_name(self):
        return self.owner.bank_name
    
    @property
    def account_name(self):
        return self.owner.account_name
    
    @property
    def account_number(self):
        return self.owner.account_number

    class Meta:
        verbose_name = "investment"
        verbose_name_plural = "investments"

    def __str__(self):
        return 'Owner: {} Farm: {} Units: {}'.format(
            self.owner,
            self.farm,
            self.units
        )

    def get_absolute_url(self):
        return reverse("investment_detail", kwargs={"pk": self.pk})
