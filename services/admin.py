from django.contrib import admin
from django.utils.safestring import mark_safe

from services.models import Service, ServiceItem


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('id', 'title',)

class ServiceItemAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'service',
        'title_image',
        'post_title_image',
        'content',
        'price',
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'post_title_image'
    ]
    list_display = ('id', 'title', 'service', 'post_title_image', 'price')
    list_display_links = ('id', 'title')
    list_editable = ('service',)
    search_fields = [
        'title',
        'service__title'
    ]
    list_filter = [
        'service__title'
    ]


    save_on_top = True

    @admin.display(description='Титульное изображение')
    def post_title_image(self, ServiceItem):
        if ServiceItem.title_image:
            return mark_safe(f"<img src='{ServiceItem.title_image.url}' width=75>")
        return 'Нет фото'

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
