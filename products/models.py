from PIL import Image
from django.db import models
from django.urls import reverse

from tags.models import Tag


class ProductCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='Slug')

    class Meta:
        db_table = 'product_category'
        verbose_name = 'Категории продуктов'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.title


class Product(models.Model):
    PRICE_CHOICE = (
        ('₽', '₽'),
        ('₽/гр', '₽/гр'),
        ('$', '$'),
        ('$/гр', '$/гр'),
        ('¥', '¥'),
        ('¥/гр', '¥/гр'),
    )

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Текст')
    size = models.CharField(max_length=100, default=None, null=True, blank=True, verbose_name='Размеры')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    price_choice = models.CharField(max_length=10, choices=PRICE_CHOICE, default='₽', null=True, blank=True,
                                    verbose_name='Значение цены')
    in_catalog = models.BooleanField(default=True, verbose_name='В каталоге')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='Category',
                                 verbose_name='Категория')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default='', null=True, blank=True,
                                    verbose_name='Титульное изображение (Квадрат min_420x420px)'
                                                 ' или прямоугольник(ширина больше высоты)')
    image1 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True,
                               verbose_name='Изображение_1 (Квадрат min_420x420px)'
                                            'или прямоугольник(ширина больше высоты)')
    image2 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True,
                               verbose_name='Изображение_2 (Квадрат min_420x420px)'
                                            'или прямоугольник(ширина больше высоты)' )
    image3 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True,
                               verbose_name='Изображение_3 (Квадрат min_420x420px)'
                                            'или прямоугольник(ширина больше высоты)')
    image4 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True,
                               verbose_name='Изображение_4 (Квадрат min_420x420px)'
                                            'или прямоугольник(ширина больше высоты)')
    image5 = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True,
                               verbose_name='Изображение_5 (Квадрат min_420x420px)'
                                            'или прямоугольник(ширина больше высоты)')
    tags_p = models.ManyToManyField(Tag, blank=True, related_name='tags_p', verbose_name='Тэги')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'slug': self.slug})
