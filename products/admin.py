from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import ProductCategory, Product

class ProductAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'size',
        'price',
        'price_choice',
        'in_catalog',
        'category',
        'tags_p',
        'title_image',
        'post_title_image',
        'get_title_image_size',
        'image1',
        'post_image1',
        'get_image1_size',
        'image2',
        'post_image2',
        'get_image2_size',
        'image3',
        'post_image3',
        'get_image3_size',
        'image4',
        'post_image4',
        'get_image4_size',
        'image5',
        'post_image5',
        'get_image5_size',
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'post_title_image',
        'get_title_image_size',
        'post_image1',
        'get_image1_size',
        'post_image2',
        'get_image2_size',
        'post_image3',
        'get_image3_size',
        'post_image4',
        'get_image4_size',
        'post_image5',
        'get_image5_size',
    ]
    list_display = ('title', 'price', 'price_choice', 'in_catalog', 'post_title_image','get_title_image_size', 'category', )
    list_display_links = ('title', 'post_title_image', )
    list_editable = ('price', 'in_catalog', 'category', 'price_choice', )
    list_per_page = 10
    search_fields = ['title', 'category__title', ]
    list_filter = ['category__title', 'in_catalog', ]
    save_on_top = True

    @admin.display(description='Титульное_изображение')
    def post_title_image(self, Product):
        if Product.title_image:
            return mark_safe(f"<img src='{Product.title_image.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_титульного_изображения')
    def get_title_image_size(self, obj):
        return (f'{obj.title_image.size / 1024:.2f} Кб')

    @admin.display(description='Изображение_1')
    def post_image1(self, Product):
        if Product.image1:
            return mark_safe(f"<img src='{Product.image1.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_изображения_1')
    def get_image1_size(self, obj):
        return (f'{obj.image1.size / 1024:.2f} Кб')

    @admin.display(description='Изображение_2')
    def post_image2(self, Product):
        if Product.image2:
            return mark_safe(f"<img src='{Product.image2.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_изображения_2')
    def get_image2_size(self, obj):
        return (f'{obj.image2.size / 1024:.2f} Кб')

    @admin.display(description='Изображение_3')
    def post_image3(self, Product):
        if Product.image3:
            return mark_safe(f"<img src='{Product.image3.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_изображения_3')
    def get_image3_size(self, obj):
        return (f'{obj.image3.size / 1024:.2f} Кб')

    @admin.display(description='Изображение_4')
    def post_image4(self, Product):
        if Product.image4:
            return mark_safe(f"<img src='{Product.image4.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_изображения_4')
    def get_image4_size(self, obj):
        return (f'{obj.image4.size / 1024:.2f} Кб')

    @admin.display(description='Изображение_5')
    def post_image5(self, Product):
        if Product.image5:
            return mark_safe(f"<img src='{Product.image5.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Размер_изображения_5')
    def get_image5_size(self, obj):
        return (f'{obj.image5.size / 1024:.2f} Кб')


class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


