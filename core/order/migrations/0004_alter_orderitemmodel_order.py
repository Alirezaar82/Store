# Generated by Django 4.2.10 on 2024-06-09 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_ordermodel_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='order.ordermodel'),
        ),
    ]
