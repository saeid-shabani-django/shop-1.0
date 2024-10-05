# Generated by Django 4.2.3 on 2024-10-04 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_image_alter_comment_body_alter_comment_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 4, 17, 4, 23, 698705)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]