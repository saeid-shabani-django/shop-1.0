from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


class Product(models.Model):
    title = models.CharField(max_length=120,verbose_name='title')
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # cover = models.ImageField(upload_to='')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.pk])




class Comment(models.Model):
    PRODUCT_STARS = {
        ('1','very bad'),
        ('2','bad'),
        ('3','good'),
        ('4','very good'),
        ('5','excellent'),
    }

    body = models.TextField()
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    stars = models.CharField(choices=PRODUCT_STARS)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    active = models.BooleanField(default=True)




