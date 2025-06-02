import random

from django import template
from django.core.cache import cache


from portfolio.models import PortfolioItem

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели PortfolioItem из БД
# используется в 'portfolio_main.html'
# базовый шаблон 'portfolio_items_list.html'
def get_portfolio_items():
    portfolio_items = PortfolioItem.objects.all()
    cache_portfolio_items = cache.get_or_set('portfolio_items', portfolio_items, 10)
    return portfolio_items

@register.simple_tag()
# Теги для отображения случайных экземпляров модели
# в количестве 9 штук для наполнения блока портфолио
# используется в 'index.html'
# базовый шаблон 'portfolio_catalog.html'
def get_random_portfolio_items_9():
    related_portfolio_items = PortfolioItem.objects.all()
    cache_portfolio_items = cache.get_or_set('related_portfolio_items', related_portfolio_items, 10)
    if len(related_portfolio_items) < 9:
        return cache_portfolio_items
    else:
        try:
            random_portfolio_items = random.sample(list(cache_portfolio_items), k=9, counts=None)
            return random_portfolio_items
        except IndexError:
            pass



