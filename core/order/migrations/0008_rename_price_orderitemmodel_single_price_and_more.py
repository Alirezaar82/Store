# Generated by Django 4.2.10 on 2024-06-09 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_orderitemmodel_singel_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitemmodel',
            old_name='price',
            new_name='single_price',
        ),
        migrations.RenameField(
            model_name='orderitemmodel',
            old_name='singel_price',
            new_name='total_price',
        ),
    ]
