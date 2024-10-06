from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from carts.cart import Cart
from products.models import Product
from .forms import OrderForm
from .models import OrderItem


@login_required()
def show_order(request):
    form = OrderForm()
    cart =Cart(request)
    if len(cart)==0:
        messages.warning(request,'your cart is empty')
        return redirect('product_list')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            main_form = form.save(commit=False)
            main_form.user = request.user
            main_form.save()

        for item in cart:
            OrderItem.objects.create(
                order = main_form,
                product= item['product_obj'],
                quantity= item['quantity'],
                price= item['product_obj'].price
            )
        cart.clear()
        request.user.first_name = main_form.first_name
        request.user.last_name = main_form.last_name
        request.user.save()



    return render(request,'orders/order_create.html',{'form':form})
