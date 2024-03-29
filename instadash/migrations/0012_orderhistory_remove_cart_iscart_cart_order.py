# Generated by Django 4.2.1 on 2023-09-08 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0011_cart_place_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=4000, null=True)),
                ('destination', models.CharField(max_length=4000, null=True)),
                ('isDelivery', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='isCart',
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instadash.orderhistory'),
        ),
    ]
