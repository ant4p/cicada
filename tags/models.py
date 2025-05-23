from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=15, db_index=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=16,db_index=True, unique=True, verbose_name="Slug")

    class Meta:
        db_table = 'tag'
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags:tag', kwargs={'slug': self.slug})
