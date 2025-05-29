from django import template
from django.core.cache import cache

from tags.models import Tag

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели Tag из БД
# используется в 'tags_main.html' и 'tag.html'
# базовый шаблон 'tag_list.html'
def get_tags():
    tags = Tag.objects.all()
    tags_cache = cache.get_or_set('tags', tags, 10)
    return tags_cache
