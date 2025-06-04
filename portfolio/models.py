from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    image = ThumbnailerImageField(upload_to='photos/%Y/%m/%d',
                                  default='', null=True, blank=True,
                                  resize_source=dict(quality=80, size=(1024, 1024)),
                                    verbose_name='Изображение (Квадрат min_420x420px) '
                                                 'или прямоугольник(ширина больше высоты)')

    class Meta:
        db_table = 'portfolio_items'
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        ordering = ['-id']

    def __str__(self):
        return self.title
