from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Content')

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services_item', kwargs={'slug': self.slug})

class ServiceItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Content')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Title_image')
    price = models.PositiveSmallIntegerField(verbose_name='Price')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='Service', verbose_name='Service')

    class Meta:
        db_table = 'service_item'

    def __str__(self):
        return self.title



