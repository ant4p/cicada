from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', default='', null=True, blank=True,
                                    verbose_name='Изображение')

    class Meta:
        db_table = 'portfolio_items'
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.title
