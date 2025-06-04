from django.db import models
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField
from PIL import ImageFile

from src.utils import generate_unique_slug

ImageFile.LOAD_TRUNCATED_IMAGES = True

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

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if not self.slug:
            self.slug = generate_unique_slug(ProductCategory, self.title)

        super(ProductCategory, self).save(*args)


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
    title_image = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                        default='', null=True, blank=True,
                                        resize_source=dict(quality=80, size=(1024, 1024)),
                                        verbose_name='Титульное изображение (Квадрат min_420x420px)'
                                                     ' или прямоугольник(ширина больше высоты)')
    image1 = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                   default=None, null=True, blank=True,
                                   resize_source=dict(quality=80, size=(1024, 1024)),
                                   verbose_name='Изображение_1 (Квадрат min_420x420px)'
                                                'или прямоугольник(ширина больше высоты)')
    image2 = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                   default=None, null=True, blank=True,
                                   resize_source=dict(quality=80, size=(1024, 1024)),
                                   verbose_name='Изображение_2 (Квадрат min_420x420px)'
                                                'или прямоугольник(ширина больше высоты)')
    image3 = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                   default=None, null=True, blank=True,
                                   resize_source=dict(quality=80, size=(1024, 1024)),
                                   verbose_name='Изображение_3 (Квадрат min_420x420px)'
                                                'или прямоугольник(ширина больше высоты)')
    image4 = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                   default=None, null=True, blank=True,
                                   resize_source=dict(quality=80, size=(1024, 1024)),
                                   verbose_name='Изображение_4 (Квадрат min_420x420px)'
                                                'или прямоугольник(ширина больше высоты)')
    image5 = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                   default=None, null=True, blank=True,
                                   resize_source=dict(quality=80, size=(1024, 1024)),
                                   verbose_name='Изображение_5 (Квадрат min_420x420px)'
                                                'или прямоугольник(ширина больше высоты)')
    tags_p = models.ManyToManyField(Tag, blank=True, related_name='tags_p', verbose_name='Тэги')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product', kwargs={'slug': self.slug})

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if not self.slug:
            self.slug = generate_unique_slug(Product, self.title)

        super(Product, self).save(*args)
