from django.utils import  timezone
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from accounts.models import CustomUser
from django.utils.translation import gettext as _


class Product(models.Model):
    title = models.CharField(max_length=120,verbose_name='title')
    description = models.TextField()
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/images/',blank=True,null=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.pk])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager,self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = {
        ('1','very bad'),
        ('2','bad'),
        ('3','good'),
        ('4','very good'),
        ('5','excellent'),
    }

    body = models.TextField(verbose_name=_('enter your comment'))
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    stars = models.CharField(choices=PRODUCT_STARS,blank=True,verbose_name='rate the product')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    active = models.BooleanField(default=True)
    objects = models.Manager()
    get_active_comments = ActiveCommentManager()
    def get_absolute_url(self):
        return reverse('product_detail',args=[self.product.id])




