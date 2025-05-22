import random

from django import template
from products.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return ProductCategory.objects.all()


@register.simple_tag()
def get_random_product_7():
    products = Product.objects.filter(in_catalog=True)
    try:
        random_products = random.choices(products, k=7)
        return random_products
    except IndexError:
        pass

@register.simple_tag()
def get_random_product_4():
    products = Product.objects.filter(in_catalog=True)
    try:
        random_products = random.choices(products, k=4)
        return random_products
    except IndexError:
        pass

@register.simple_tag()
def get_random_product_2():
    products = Product.objects.filter(in_catalog=True).select_related('category').prefetch_related()
    try:
        random_products = random.choices(products, k=2)
        return random_products
    except IndexError:
        pass

@register.simple_tag()
def get_products():
    return Product.objects.filter(in_catalog=True)





