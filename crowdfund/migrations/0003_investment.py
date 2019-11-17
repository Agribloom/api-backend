# Generated by Django 2.2.6 on 2019-11-12 16:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crowdfund', '0002_auto_20191106_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinLengthValidator(1)])),
                ('amount_currency', djmoney.models.fields.CurrencyField(choices=[('NGN', 'NGN ₦')], default='NGN', editable=False, max_length=3)),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='NGN', max_digits=14)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crowdfund.Farm')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'investment',
                'verbose_name_plural': 'investments',
            },
        ),
    ]