# Generated by Django 4.2.1 on 2023-08-17 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0007_dashboard_forhome_location_categorydashboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='forHome',
            field=models.BooleanField(default=True),
        ),
    ]
