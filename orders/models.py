from django.db import models
from django.conf import settings

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='items')
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=700)
    is_paid = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datatime_modified = models.DateTimeField(auto_now=True)
    add_note = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem: {self.id} , order: {self.order.id}'






