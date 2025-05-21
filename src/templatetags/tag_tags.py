from django import template

from tags.models import Tag

register = template.Library()

@register.simple_tag()
def get_tags():
    return Tag.objects.all()