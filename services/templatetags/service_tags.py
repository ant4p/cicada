from django import template
from services.models import *

register = template.Library()

@register.simple_tag()
def get_services():
    return Service.objects.all()

@register.simple_tag()
def get_services_items():
    return ServiceItem.objects.all()

