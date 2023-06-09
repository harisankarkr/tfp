# Generated by Django 4.1.7 on 2023-04-04 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_rename_customer_customerprofile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_name', models.CharField(max_length=255)),
                ('category1', models.CharField(max_length=255)),
                ('category2', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fit', models.CharField(max_length=255)),
                ('care', models.CharField(max_length=255)),
                ('material', models.CharField(max_length=255)),
                ('occasion', models.CharField(max_length=255)),
                ('image1', models.ImageField(upload_to='product_images/')),
                ('image2', models.ImageField(blank=True, upload_to='product_images/')),
                ('image3', models.ImageField(blank=True, upload_to='product_images/')),
                ('image4', models.ImageField(blank=True, upload_to='product_images/')),
                ('small', models.PositiveIntegerField()),
                ('medium', models.PositiveIntegerField()),
                ('large', models.PositiveIntegerField()),
                ('extra_large', models.PositiveIntegerField()),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.designer')),
            ],
            options={
                'unique_together': {('prd_name', 'designer')},
            },
        ),
    ]
