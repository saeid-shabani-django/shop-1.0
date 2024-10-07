# Generated by Django 4.2.3 on 2024-10-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_comment_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(blank=True, choices=[('1', 'very bad'), ('5', 'excellent'), ('2', 'bad'), ('4', 'very good'), ('3', 'good')], verbose_name='rate the product'),
        ),
    ]
