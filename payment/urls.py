from django.urls import path
from . import views



urlpatterns = [
    path('process/',views.payment_process,name='payment_process'),
    path('callback/',views.callback_payment,name='callback_payment'),

]





