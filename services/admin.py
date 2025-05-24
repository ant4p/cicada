from django.contrib import admin
from django.utils.safestring import mark_safe

from services.models import Service, ServiceItem


class ServiceAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content'
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)
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
        'tags_s',
        'content',
        'price',
        'show_contacts',
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'post_title_image'
    ]
    list_display = ('title', 'service','show_contacts', 'post_title_image', 'price', )
    list_display_links = ('title', )
    list_per_page = 10
    list_editable = ('service', 'show_contacts', 'price', )
    search_fields = [
        'title',
        'service__title',
    ]
    list_filter = [
        'service__title',
        'show_contacts',
    ]
    save_on_top = True


    @admin.display(description='Титульное изображение')
    def post_title_image(self, ServiceItem):
        if ServiceItem.title_image:
            return mark_safe(f"<img src='{ServiceItem.title_image.url}' width=75>")
        return 'Нет фото'

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
