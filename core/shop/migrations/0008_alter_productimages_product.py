# Generated by Django 4.2.10 on 2024-06-14 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_productimages_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='shop.productmodel', verbose_name='product'),
        ),
    ]
