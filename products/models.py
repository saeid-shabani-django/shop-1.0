from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120,verbose_name='title')
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # cover = models.ImageField(upload_to='')
