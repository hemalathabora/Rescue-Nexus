# Generated by Django 5.0.7 on 2025-03-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_app', '0014_medicalrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '😡 Very Bad'), (2, '🙁 Bad'), (3, '😐 Neutral'), (4, '🙂 Good'), (5, '😍 Excellent')])),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
