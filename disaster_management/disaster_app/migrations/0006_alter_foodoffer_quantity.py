# Generated by Django 5.0.7 on 2025-03-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_app', '0005_foodoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodoffer',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
