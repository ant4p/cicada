

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from products.models import Product


class ProductsListView(ListView):
    template_name = 'products/products_main.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        return Product.objects.all()

class ProductView(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Product.objects.filter(product__slug=self.kwargs['slug'])
