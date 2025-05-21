from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from products.models import Product
from tags.models import Tag


class TagsListView(ListView):
    template_name = 'tags/tags_main.html'
    context_object_name = 'tags_list'

    def get_queryset(self):
        return Tag.objects.all()

class TagView(ListView):
    template_name = 'tags/tag.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Product.objects.filter(tags__slug=self.kwargs['slug'], in_catalog=True)

