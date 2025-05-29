from django import template
from django.core.cache import cache

from src.models import Contacts

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели ProductCategory из БД
# используется в contacts. Закэшировано на 10 секунд.

def get_contacts():
    contacts = Contacts.objects.filter()
    cache_contacts = cache.get_or_set('contacts', contacts, 10)
    return cache_contacts