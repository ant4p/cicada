from django.contrib import admin
from django.utils.safestring import mark_safe

from services.models import Service, ServiceItem


class ServiceAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content'
    ]
    list_display = ('title',)
    readonly_fields = [
        'slug',
    ]
    list_display_links = ('title',)
    list_per_page = 10
    search_fields = ['title', ]
    save_on_top = True

class ServiceItemAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'service',
        'title_image',
        'post_title_image',
        'get_title_image_size',
        'tags_s',
        'content',
        'price',
        'price_choice',
        'show_contacts',
    ]
    readonly_fields = [
        'post_title_image',
        'get_title_image_size',
        'slug',
    ]
    list_display = (
        'title',
        'service',
        'show_contacts',
        'post_title_image',
        'get_title_image_size',
        'price',
        'price_choice',
    )
    list_display_links = ('title', )
    list_per_page = 10
    list_editable = ('service', 'show_contacts', 'price', 'price_choice', )
    search_fields = [
        'title',
        'service__title',
    ]
    list_filter = [
        'service__title',
        'show_contacts',
        'price_choice',
    ]
    save_on_top = True


    @admin.display(description='Титульное изображение')
    def post_title_image(self, ServiceItem):
        if ServiceItem.title_image:
            return mark_safe(f"<img src='{ServiceItem.title_image.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер')
    def get_title_image_size(self, obj):
        return (f'{obj.title_image.size / 1024:.2f} Кб')

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
