from django.db import models
from django.urls import reverse

from tags.models import Tag


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Текст')

    class Meta:
        db_table = 'service'
        verbose_name = 'Вид Услуги'
        verbose_name_plural = 'Виды Услуг'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:services_item', kwargs={'slug': self.slug})

class ServiceItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Текст')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Изображение (Квадрат min_420x420px)')
    price = models.PositiveSmallIntegerField(verbose_name='Цена', blank=True, null=True)
    show_contacts = models.BooleanField(verbose_name="Показать контакты", default=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='Service', verbose_name='Относится к услуге')
    tags_s = models.ManyToManyField(Tag, blank=True, related_name='tags_s', verbose_name='Тэги')

    class Meta:
        db_table = 'serviceitem'
        verbose_name = 'Наполнение услуги'
        verbose_name_plural = 'Наполнение услуги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:services_item', kwargs={'slug': self.slug})





