# Generated by Django 4.2.1 on 2023-08-30 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0010_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='place_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
