# Generated by Django 4.2.3 on 2024-10-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_add_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
