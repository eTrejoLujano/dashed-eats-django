# Generated by Django 4.2.1 on 2023-08-03 07:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0005_alter_ad_description_alter_item_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='ads',
            new_name='stores',
        ),
        migrations.AddField(
            model_name='category',
            name='stores',
            field=models.ManyToManyField(through='instadash.StoreCategory', to='instadash.store'),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='stores',
            field=models.ManyToManyField(through='instadash.StoreDashboard', to='instadash.store'),
        ),
        migrations.AddField(
            model_name='foodtype',
            name='stores',
            field=models.ManyToManyField(through='instadash.StoreType', to='instadash.store'),
        ),
        migrations.AddField(
            model_name='item',
            name='users',
            field=models.ManyToManyField(through='instadash.Cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='store',
            name='users',
            field=models.ManyToManyField(through='instadash.SavedStore', to=settings.AUTH_USER_MODEL),
        ),
    ]
