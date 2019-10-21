from django.db import models
from django.urls import reverse
from django.conf import settings
from djmoney.models.fields import MoneyField

class PManager(models.Model):

    ROLE_TYPE = (
        ('P', 'Project Manager'),
        ('F', 'Farm Manager')
    )
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_TYPE)

    class Meta:
        verbose_name = "project and farm manager"
        verbose_name_plural = "project and farm managers"

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
        return reverse("category_detail", kwargs={"pk": self.slug})


class Project(models.Model):

    PROJECT_STATUS = (
        ('open', 'Open'),
        ('close', 'Closed')
    )

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    project_manger = models.ForeignKey(PManager, verbose_name='project manager', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=150)
    insurance_statement = models.TextField()
    insured = models.BooleanField(default=True)
    units = models.PositiveIntegerField()
    unit_in_stock = models.PositiveIntegerField()
    price_per_unit = MoneyField(max_digits=14, decimal_places=2, default_currency='NGN')
    roi = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='images/farm/%Y/')
    start_date = models.DateField()
    end_date = models.DateField()


    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


class Farm(Project):

    stage = models.CharField('farm stage', max_length=50)
    harvest_date = models.DateField()


    class Meta:
        verbose_name = "farm"
        verbose_name_plural = "farms"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("farm_detail", kwargs={"pk": self.pk})
