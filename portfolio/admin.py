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
        'post_image',
    ]
    prepopulated_fields = {'slug': ('title', )}
    readonly_fields = [
        'post_image',
    ]
    list_display = ('title', 'post_image', )
    list_display_links = ('title', )
    list_per_page = 10
    search_fields = [
        'title',
    ]
    save_on_top = True

    @admin.display(description='Изображениеэ')
    def post_image(self, PortfolioItem):
        if PortfolioItem.image:
            return mark_safe(f"<img src='{PortfolioItem.image.url}' width=75>")
        return 'Нет фото'

admin.site.register(PortfolioItem, PortfolioItemAdmin)
