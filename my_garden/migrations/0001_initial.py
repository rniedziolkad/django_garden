# Generated by Django 4.1.4 on 2023-01-22 19:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('watering_level', models.CharField(choices=[('low', 'skąpe'), ('medium', 'umiarkowane'), ('high', 'obfite'), ('very_high', 'bardzo obfite')], max_length=32)),
                ('watering_period', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_watering', models.DateTimeField(default=datetime.datetime(2023, 1, 22, 20, 23, 9, 198284))),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_garden.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]