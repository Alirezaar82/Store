# Generated by Django 4.2.10 on 2024-06-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddressmodel',
            name='name',
            field=models.CharField(default='ادرس من', max_length=255),
        ),
    ]
