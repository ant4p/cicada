from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField

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
    PRICE_CHOICE = (
        ('₽', '₽'),
        ('₽/гр', '₽/гр'),
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Текст')
    title_image = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                        default=None, null=True, blank=True,
                                        resize_source=dict(quality=80, size=(1024, 1024)),
                                        verbose_name='Изображение (Квадрат min_420x420px)'
                                                     'или прямоугольник(ширина больше высоты)')
    price = models.PositiveSmallIntegerField(verbose_name='Цена', blank=True, null=True)
    price_choice = models.CharField(max_length=10, choices=PRICE_CHOICE,
                                    default='Р', null=True, blank=True, verbose_name='Значение цены')
    show_contacts = models.BooleanField(verbose_name="Показать контакты", default=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT,
                                related_name='Service', verbose_name='Относится к услуге')
    tags_s = models.ManyToManyField(Tag, blank=True, related_name='tags_s', verbose_name='Тэги')

    class Meta:
        db_table = 'service_item'
        verbose_name = 'Наполнение услуги'
        verbose_name_plural = 'Наполнение услуги'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:services_item', kwargs={'slug': self.slug})





