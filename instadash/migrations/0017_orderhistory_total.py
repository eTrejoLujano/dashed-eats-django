# Generated by Django 4.2.1 on 2023-09-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0016_remove_orderhistory_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='Total',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
    ]
