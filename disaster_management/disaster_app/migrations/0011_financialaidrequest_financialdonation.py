# Generated by Django 5.0.7 on 2025-03-20 02:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_app', '0010_volunteer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialAidRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('reason', models.TextField()),
                ('amount_needed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_mode', models.CharField(choices=[('UPI', 'UPI'), ('Bank Transfer', 'Bank Transfer'), ('PayPal', 'PayPal'), ('Other', 'Other')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_donated', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('UPI', 'UPI'), ('Bank Transfer', 'Bank Transfer'), ('PayPal', 'PayPal'), ('Other', 'Other')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('aid_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disaster_app.financialaidrequest')),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
