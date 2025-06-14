from django.db import models
from django.urls import reverse

from src.utils import generate_unique_slug


class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=55,db_index=True, unique=True, verbose_name="Slug")

    class Meta:
        db_table = 'tag'
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags:tag', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = generate_unique_slug(Tag, self.title)
        super().save(*args, **kwargs)

