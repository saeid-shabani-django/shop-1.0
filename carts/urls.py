from django.urls import path
from . import views


urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:product_id>/',views.remove_from_cart,name='remove'),
    path('clear/',views.empty_the_cart,name='emptythecart'),
]