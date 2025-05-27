import random

from django import template
from products.models import *

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели ProductCategory из БД
# используется в 'products_main.html'
# базовый шаблон 'category_list.html'
def get_categories():
    return ProductCategory.objects.all()


@register.simple_tag()
# Тег для отображения случайных экземпляров модели
# в количестве 7 штук для продуктов из каталога
# используется в 'index.html' и 'cooperation.html'
# базовый шаблон 'index_catalog_7.html'
def get_random_product_7():
    products = Product.objects.filter(in_catalog=True)
    if len(products) < 7:
        return products
    else:
        try:
            random_products = random.choices(products, k=7)
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
    try:
        random_products = random.choices(products, k=4)
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
    try:
        random_products = random.choices(products, k=2)
        return random_products
    except IndexError:
        pass
