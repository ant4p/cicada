from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Content')

    class Meta:
        db_table = 'service'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:services_item', kwargs={'slug': self.slug})

class ServiceItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Content')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Title_image')
    price = models.PositiveSmallIntegerField(verbose_name='Price', blank=True, null=True)
    show_contacts = models.BooleanField(verbose_name="Show_contacts", default=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='Service', verbose_name='Service')

    class Meta:
        db_table = 'service_item'
        verbose_name = 'Наполнение услуги'
        verbose_name_plural = 'Наполнение услуги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:services_item', kwargs={'slug': self.slug})





