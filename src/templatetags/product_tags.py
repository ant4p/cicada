import random
from django import template
from django.core.cache import cache

from products.models import *

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели ProductCategory из БД
# используется в 'products_main.html'
# базовый шаблон 'category_list.html'
def get_categories():
    categories = ProductCategory.objects.all()
    cache_product_category = cache.get_or_set('categories', categories, 10)
    return cache_product_category


@register.simple_tag()
# Тег для отображения случайных экземпляров модели
# в количестве 7 штук для продуктов из каталога
# используется в 'index.html' и 'cooperation.html'
# базовый шаблон 'index_catalog_7.html'
def get_random_product_7():
    products = Product.objects.filter(in_catalog=True)
    products_cache = cache.get_or_set('products', products, 10)
    if len(products) < 7:
        return products_cache
    else:
        try:
            random_products = random.choices(products_cache, k=7)
            return random_products
        except IndexError:
            pass


@register.simple_tag()
# Тег для отображения случайных экземпляров модели
# в количестве 4 штук для продуктов из каталога
# используется в карточке каждого продукта в 'product.html'
# базовый шаблон 'see_also_products.html'
def get_random_product_4():
    products = Product.objects.filter(in_catalog=True)
    products_cache = cache.get_or_set('products', products, 10)
    try:
        random_products = random.choices(products_cache, k=4)
        return random_products
    except IndexError:
        pass


@register.simple_tag()
# Тег для отображения случайных экземпляров модели
# в количестве 2 штук для продуктов из каталога
# используется в 'index.html' с переходом в каталог
# базовый шаблон 'index_catalog_2.html'
def get_random_product_2():
    products = Product.objects.filter(in_catalog=True).select_related('category')
    products_cache = cache.get_or_set('products', products, 10)
    try:
        random_products = random.choices(products_cache, k=2)
        return random_products
    except IndexError:
        pass
