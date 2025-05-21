from django.views.generic import ListView, DetailView
from django.urls import reverse

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


    def get_success_url(self):
        return reverse('product', kwargs={'slug': self.object.slug})

