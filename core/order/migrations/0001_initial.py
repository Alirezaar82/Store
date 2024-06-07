# Generated by Django 4.2.10 on 2024-06-07 15:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_productmodel_avg_rate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('discount_percent', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('max_limit_usage', models.PositiveIntegerField(default=10)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('used_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datetime_created'],
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'pending'), (2, 'success'), (3, 'faild')], default=1)),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip_code', models.CharField(default='0')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('coupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='order.couponmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-datetime_created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_update', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.ordermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.productmodel')),
            ],
            options={
                'ordering': ['-datetime_created'],
            },
        ),
    ]
