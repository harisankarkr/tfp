# Generated by Django 4.1.7 on 2023-04-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0002_alter_product_designer_alter_product_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='media/product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='media/product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, upload_to='media/product_images/'),
        ),
    ]
