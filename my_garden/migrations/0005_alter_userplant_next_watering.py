# Generated by Django 4.1.4 on 2023-01-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_garden', '0004_alter_userplant_next_watering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplant',
            name='next_watering',
            field=models.DateTimeField(null=True),
        ),
    ]
