from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
import requests
from orders.models import Order
import json

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,pk=order_id)
    toman_total_price = Order.get_total_price()
    rial_total_price = toman_total_price * 10
    request_header={
        'accept':'application/json',
        'content_type':'application/json',
    }
    request_data={
        'merchant_id':settings.django_merchant_id,
        'amount':rial_total_price,
        'description':f'{order.user.first_name} last name: {order.user.last_name}',
        'callback_url': request.build_absolute_uri(reverse('callback_payment'))

    }
    res = requests.post(url='https://payment.zarinpal.com/pg/v4/payment/request.json',
                        data=json.dumps(request_data),
                        headers=request_header)
    data= res.json()['data']
    authority = data['authority']
    order.authority = authority
    order.save()

    if 'errors' not in data or len(res.json()['errors']) == 0:
        return redirect(f'https://payment.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse('there is a error from zarinpal')


def callback_payment(request):
    payment_status = request.GET.get('status')
    payment_authority = request.GET.get('authority')

    order = get_object_or_404(Order,authority = payment_authority)
    toman_total_price = Order.get_total_price()
    rial_total_price = toman_total_price * 10
    request_header = {
        'accept': 'application/json',
        'content_type': 'application/json',
    }
    request_data = {
        'merchant_id': 'merchant_id_from_zarinpal',
        'amount': rial_total_price,
        'authority': payment_authority,
    }
    if payment_status == 'OK':
        res = requests.post(url='',data=json.dumps(request_data),headers=request_header)
        if 'data' in res.json() and ('errors' not in res.json()['data'] or len(res['errors'])==0):
            data = res.json()['data']
            payment_code = data['code']
            if payment_code==100:
                order.is_paid =True
                ref_id = data['ref_id']
                order.ref_id = ref_id
                order.save()

            elif payment_code == 101:
                return HttpResponse('you have paid before')
            else:
                errors = res.json()['errors']['message']
                return HttpResponse(f'there is an error{errors}')
    else:
        return HttpResponse('not ok')

















