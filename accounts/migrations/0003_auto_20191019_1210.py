# Generated by Django 2.2.6 on 2019-10-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191019_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name='date of birth'),
        ),
    ]
