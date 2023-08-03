# Generated by Django 4.2.1 on 2023-08-02 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadash', '0003_remove_store_rating_score_remove_store_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(null=True, upload_to='src/assets/ads'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='src/assets/category'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='image',
            field=models.ImageField(null=True, upload_to='src/assets/foodtype'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='src/assets/items'),
        ),
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(null=True, upload_to='src/assets/store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(null=True, upload_to='src/assets/store/logo'),
        ),
    ]