from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib import messages


from products.forms import CommentForm
from products.models import Product, Comment



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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    def form_valid(self, form):
       obj = form.save(commit=False)
       obj.author = self.request.user
       product_id = int(self.kwargs['pk'])
       obj.product = get_object_or_404(Product,pk=product_id)

       return super().form_valid(form)







