# Generated by Django 4.2.10 on 2024-06-18 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_ordermodel_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='order.couponmodel'),
        ),
    ]
