from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from articles.models import Article
from products.models import Product
from services.models import ServiceItem
from tags.models import Tag


class TagsListView(ListView):
    template_name = 'tags/tags_main.html'
    context_object_name = 'tags_list'

    def get_queryset(self):
        return Tag.objects.all()

class TagView(ListView):
    template_name = 'tags/tag.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles_data'] = (Article.objects.filter(tags_a__slug=self.kwargs['slug'], is_published=True).
                                    prefetch_related('tags_a'))
        context['products_data'] = (Product.objects.filter(tags_p__slug=self.kwargs['slug'], in_catalog=True).
                                    prefetch_related('tags_p'))
        context['services_data'] = (ServiceItem.objects.filter(tags_s__slug=self.kwargs['slug']).
                                    prefetch_related('tags_s'))
        return context

    def get_queryset(self):
        pass


