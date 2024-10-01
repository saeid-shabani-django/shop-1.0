from django.shortcuts import render

from carts.cart import Cart


def cart_detail(request):
    carts = Cart(request)
    return render(request,'carts/cart_detail.html',{'carts':carts})
