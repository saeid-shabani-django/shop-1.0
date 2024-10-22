# Generated by Django 4.2.3 on 2024-10-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_comment_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(blank=True, choices=[('5', 'excellent'), ('3', 'good'), ('4', 'very good'), ('2', 'bad'), ('1', 'very bad')], verbose_name='rate the product'),
        ),
    ]
