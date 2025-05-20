import random
from django import template
from services.models import *

register = template.Library()

@register.simple_tag()
def get_services():
    return Service.objects.all()

@register.simple_tag()
def get_services_items():
    return ServiceItem.objects.all()

# Делаем теги для случайного отображения экземпляров объектов для услуги №2
# и вывода наименования этой услуги

@register.simple_tag()
def get_random_services_1_9():
    services = ServiceItem.objects.filter(service__pk=1)
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
    services = ServiceItem.objects.filter(service__pk=1)
    try:
        random_services = random.choices(services, k=1)
        return random_services
    except IndexError:
        pass



# Делаем теги для случайного отображения экземпляров объектов для услуги №3
# и вывода наименования этой услуги

@register.simple_tag()
def get_random_services_2_9():
    services = ServiceItem.objects.filter(service__pk=2)
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
    services = ServiceItem.objects.filter(service__pk=2)
    try:
        random_services = random.choices(services, k=1)
        return random_services
    except IndexError:
        pass




