# Generated by Django 4.2.3 on 2023-07-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='no_image.jpg', upload_to='prod_img'),
        ),
    ]
