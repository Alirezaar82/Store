# Generated by Django 4.2.10 on 2024-06-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_productmodel_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='sold',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
