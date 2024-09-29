from django.shortcuts import render
from django.views import generic

from products.models import Product


class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    # model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    # def get_queryset(self):
    #     return Product.objects.filter(active=True)


class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    model = Product


