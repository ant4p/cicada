from django.core.cache import cache
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
        articles = (Article.objects.filter(tags_a__slug=self.kwargs['slug'], is_published=True).
                                    prefetch_related('tags_a'))
        # cache_articles = cache.get_or_set('articles', articles, 10)
        context['articles_data'] = articles
        products = (Product.objects.filter(tags_p__slug=self.kwargs['slug'], in_catalog=True).
                                    prefetch_related('tags_p'))
        # cache_products = cache.get_or_set('products', products, 10)
        context['products_data'] = products
        services = (ServiceItem.objects.filter(tags_s__slug=self.kwargs['slug']).select_related('service').
                                    prefetch_related('tags_s'))
        # cache_services = cache.get_or_set('services', services, 10)
        context['services_data'] = services
        return context

    def get_queryset(self):
        pass


