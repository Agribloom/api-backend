# Generated by Django 2.2.6 on 2019-12-20 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfund', '0008_remove_farm_manger'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmmanager',
            name='farm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crowdfund.Farm'),
        ),
    ]