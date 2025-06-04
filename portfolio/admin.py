from django.contrib import admin
from django.utils.safestring import mark_safe

from portfolio.models import PortfolioItem
from services.models import ServiceItem


# Register your models here.
class PortfolioItemAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'image',
        'get_size',
        'post_image',
    ]
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = [
        'post_image',
        'get_size',
    ]
    list_display = ('title', 'post_image', 'get_size', )
    list_display_links = ('title', )
    list_per_page = 10
    search_fields = [
        'title',
    ]
    save_on_top = True

    @admin.display(description='Изображение')
    def post_image(self, PortfolioItem):
        if PortfolioItem.image:
            return mark_safe(f"<img src='{PortfolioItem.image.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер')
    def get_size(self, obj):
        return (f'{obj.image.size / 1024:.2f} Кб')

admin.site.register(PortfolioItem, PortfolioItemAdmin)
