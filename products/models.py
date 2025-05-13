from django.db import models
from django.urls import reverse

class ProductCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='Slug')

    class Meta:
        db_table = 'product_category'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Текст')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='Category', verbose_name='Категория')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Титульное изображение')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='image1')
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='image2')
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='image3')
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='image4')
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='image5')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'slug': self.slug})

