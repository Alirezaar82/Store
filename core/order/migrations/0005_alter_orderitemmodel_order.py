# Generated by Django 4.2.10 on 2024-06-09 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitemmodel_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.ordermodel'),
        ),
    ]
