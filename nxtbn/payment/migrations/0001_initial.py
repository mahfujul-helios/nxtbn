# Generated by Django 4.2.11 on 2024-05-24 18:39

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('CREDIT_CARD', 'Credit Card'), ('PAYPAL', 'PayPal'), ('BANK_TRANSFER', 'Bank Transfer'), ('CASH_ON_DELIVERY', 'Cash on Delivery')], max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('payment_status', models.CharField(choices=[('AUTHORIZED', 'Authorized'), ('CAPTURED', 'Captured'), ('FAILED', 'Failed'), ('REFUNDED', 'Refunded'), ('CANCELED', 'Canceled')], default='AUTHORIZED', max_length=20)),
                ('payment_amount', models.DecimalField(decimal_places=3, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('gateway_response_raw', models.JSONField(blank=True, null=True)),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('payment_plugin_id', models.CharField(blank=True, max_length=100, null=True)),
                ('gateway_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('gateway_customer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('gateway_payment_method_id', models.CharField(blank=True, max_length=255, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('payment_plugin_id', models.CharField(blank=True, max_length=100, null=True)),
                ('gateway_name', models.CharField(blank=True, max_length=100, null=True)),
                ('card_last4', models.CharField(blank=True, max_length=4, null=True, verbose_name='Last 4 Digits')),
                ('card_exp_month', models.CharField(blank=True, max_length=2, null=True, verbose_name='Expiry Month')),
                ('card_exp_year', models.CharField(blank=True, max_length=4, null=True, verbose_name='Expiry Year')),
                ('card_brand', models.CharField(blank=True, max_length=20, null=True, verbose_name='Card Brand')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]