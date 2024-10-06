from django import forms
from .models import Order,OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =['first_name','last_name','phone_number','address','add_note']
