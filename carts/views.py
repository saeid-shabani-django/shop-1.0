from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .forms import AddToCartProductForm
from carts.cart import Cart
from products.models import Product
from django.views.decorators.http import require_POST

def cart_detail(request):
    carts = Cart(request)
    for item in carts:
        item['replace_quantity']= AddToCartProductForm(initial={
            'quantity':item['quantity'],
            'inplace':True,
        })
    return render(request,'carts/cart_detail.html',{'carts':carts})

@require_POST
def add_to_cart(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk = product_id)
    form = AddToCartProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = int(cleaned_data['quantity'])

        cart.add(product,quantity,cleaned_data['inplace'])

    return redirect('cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    cart.remove(product)
    return redirect('cart_detail')


