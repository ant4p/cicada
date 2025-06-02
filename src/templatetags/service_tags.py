import random
from django import template
from django.core.cache import cache
from services.models import *

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели Service из БД
# используется в 'services_main.html' и 'service.html'
# базовый шаблон 'services_list.html'
def get_services():
    services = Service.objects.all()
    cache_services = cache.get_or_set('services', services, 10)
    return cache_services



@register.simple_tag()
# Теги для отображения случайных экземпляров модели
# в количестве 9 штук для наполнения сервисов(3D моделирование)
# используется в 'index.html'
# базовый шаблон 'services_catalog_1.html'
def get_random_services_1_9():
    related_services = Service.objects.all()
    cache_services = cache.get_or_set('related_services', related_services, 10)
    try:
        element = cache_services[0]
        services = ServiceItem.objects.filter(service=element).select_related('service')
    except:
        services = []
    if len(services) <= 9:
        return services
    else:
        try:
            random_services = random.sample(list(services), k=9, counts=None)
            return random_services
        except IndexError:
            pass


@register.simple_tag()
def get_random_services_for_title_1():
    related_services = Service.objects.all()
    try:
        element = related_services[0]
        services = ServiceItem.objects.filter(service=element).select_related('service')
    except IndexError:
        services = []
    try:
        random_services = random.choices(services, k=1)
        return random_services
    except IndexError:
        pass


@register.simple_tag()
# Теги для отображения случайных экземпляров модели
# в количестве 9 штук для наполнения сервисов(3D визуализация)
# используется в 'index.html'
# базовый шаблон 'services_catalog_2.html'
def get_random_services_2_9():
    related_services= Service.objects.all()
    cache_services = cache.get_or_set('related_services', related_services, 10)
    try:
        element = cache_services[1]
        services = ServiceItem.objects.filter(service=element).select_related('service')
    except IndexError:
        services = []

    if len(services) <= 9:
        return services
    else:
        try:
            random_services = random.sample(list(services), k=9, counts=None)
            return random_services
        except IndexError:
            pass

@register.simple_tag()
def get_random_services_for_title_2():
    related_services = Service.objects.all()
    try:
        element = related_services[1]
        services = ServiceItem.objects.filter(service=element).select_related('service')
    except IndexError:
        services = []

    try:
        random_services = random.choices(services, k=1)
        return random_services
    except IndexError:
        pass




