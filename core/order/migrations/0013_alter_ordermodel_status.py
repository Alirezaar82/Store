# Generated by Django 4.2.10 on 2024-06-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_ordermodel_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'success'), (3, 'failed')], default=1),
        ),
    ]
