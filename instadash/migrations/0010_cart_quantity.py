# Generated by Django 4.2.1 on 2023-08-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0009_location_date_accessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
