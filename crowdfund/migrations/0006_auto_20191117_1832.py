# Generated by Django 2.2.6 on 2019-11-17 17:32

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfund', '0005_auto_20191117_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='price_per_unit',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='NGN', max_digits=14),
        ),
        migrations.AlterField(
            model_name='farm',
            name='raised',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='NGN', max_digits=14),
        ),
    ]
