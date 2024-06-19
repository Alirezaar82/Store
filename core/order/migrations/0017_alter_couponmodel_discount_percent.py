# Generated by Django 4.2.10 on 2024-06-18 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_ordermodel_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponmodel',
            name='discount_percent',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(100)]),
        ),
    ]