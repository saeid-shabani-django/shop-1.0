from django.contrib import admin

from orders.models import Order, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','is_paid']



