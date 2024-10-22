# Generated by Django 4.2.3 on 2024-10-04 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_datetime_created_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(blank=True, choices=[('3', 'good'), ('4', 'very good'), ('2', 'bad'), ('1', 'very bad'), ('5', 'excellent')], verbose_name='rate the product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
