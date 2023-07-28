# Generated by Django 4.2.1 on 2023-07-27 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='files/ad')),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='files/ad')),
            ],
        ),
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instadash.foodtype')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instadash.store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreDashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instadash.dashboard')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instadash.store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instadash.category')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instadash.store')),
            ],
        ),
    ]
