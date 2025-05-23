from django.db import models
from django.urls import reverse

from tags.models import Tag


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True,db_index=True, verbose_name='Slug')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Титульное изображение (Абстракция Высокое_качество)')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    tags_a = models.ManyToManyField(Tag, blank=True, related_name='tags_a', verbose_name='Тэги')
    content = models.TextField(blank=True, verbose_name='Текст статьи')

    class Meta:
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article', kwargs={'slug': self.slug})
