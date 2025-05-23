import random
from django import template
from services.models import *

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели Service из БД
# используется в 'services_main.html' и 'service.html'
# базовый шаблон 'services_list.html'
def get_services():
    return Service.objects.all()


@register.simple_tag()
# Теги для отображения случайных экземпляров модели
# в количестве 9 штук для наполнения сервисов(3D моделирование)
# используется в 'index.html'
# базовый шаблон 'services_catalog_1.html'
def get_random_services_1_9():
    services = ServiceItem.objects.filter(service__pk=1).select_related('service')
    if len(services) < 9:
        return services
    else:
        try:
            random_services = random.choices(services, k=9)
            return random_services
        except IndexError:
            pass

@register.simple_tag()
def get_random_services_for_title_1():
    services = ServiceItem.objects.filter(service__pk=1).select_related('service')
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
    services = ServiceItem.objects.filter(service__pk=2).select_related('service')
    if len(services) < 9:
        return services
    else:
        try:
            random_services = random.choices(services, k=9)
            return random_services
        except IndexError:
            pass

@register.simple_tag()
def get_random_services_for_title_2():
    services = ServiceItem.objects.filter(service__pk=2).select_related('service')
    try:
        random_services = random.choices(services, k=1)
        return random_services
    except IndexError:
        pass




