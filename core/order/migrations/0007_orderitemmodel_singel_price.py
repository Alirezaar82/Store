# Generated by Django 4.2.10 on 2024-06-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_couponmodel_used_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemmodel',
            name='singel_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]