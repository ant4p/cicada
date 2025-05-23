from django import template

from tags.models import Tag

register = template.Library()

@register.simple_tag()
# Тег для отображения всех экземпляров модели Tag из БД
# используется в 'tags_main.html' и 'tag.html'
# базовый шаблон 'tag_list.html'
def get_tags():
    return Tag.objects.all()
