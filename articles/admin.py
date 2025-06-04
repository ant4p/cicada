from django.contrib import admin
from django.utils.safestring import mark_safe

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'title_image',
        'post_title_image',
        'get_title_image_size',
        'is_published',
        'tags_a',
        'content',
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'post_title_image',
        'get_title_image_size',
    ]
    list_display = ('title', 'is_published', 'post_title_image', 'get_title_image_size', )
    list_display_links = ('title', )
    list_editable = ('is_published', )
    list_per_page = 10
    search_fields = ['title', ]
    list_filter = ['is_published', ]
    save_on_top = True



    @admin.display(description='Титульное изображение')
    def post_title_image(self, Article):
        if Article.title_image:
            return mark_safe(f"<img src='{Article.title_image.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_титульного_изображения')
    def get_title_image_size(self, obj):
        return (f'{obj.title_image.size / 1024:.2f} Кб')


admin.site.register(Article, ArticleAdmin)