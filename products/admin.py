from django.contrib import admin
from django.utils.safestring import mark_safe

from products.models import ProductCategory, Product

class ProductAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'price',
        'category',
        'title_image',
        'post_title_image',
        'image1',
        'post_image1',
        'image2',
        'post_image2',
        'image3',
        'post_image3',
        'image4',
        'post_image4',
        'image5',
        'post_image5'
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = [
        'post_title_image',
        'post_image1',
        'post_image2',
        'post_image3',
        'post_image4',
        'post_image5'
    ]
    list_display = ('id', 'title', 'price', 'post_title_image', 'category')
    list_display_links = ('id', 'title')
    list_editable = ('price',)
    list_per_page = 10
    search_fields = ['title', 'category__title']
    list_filter = ['category__title']
    save_on_top = True

    @admin.display(description='Титульное изображение')
    def post_title_image(self, Product):
        if Product.title_image:
            return mark_safe(f"<img src='{Product.title_image.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Изображение_1')
    def post_image1(self, Product):
        if Product.image1:
            return mark_safe(f"<img src='{Product.image1.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Изображение_2')
    def post_image2(self, Product):
        if Product.image2:
            return mark_safe(f"<img src='{Product.image1.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Изображение_3')
    def post_image3(self, Product):
        if Product.image3:
            return mark_safe(f"<img src='{Product.image1.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Изображение_4')
    def post_image4(self, Product):
        if Product.image4:
            return mark_safe(f"<img src='{Product.image1.url}' width=75>")
        return 'Нет фото'

    @admin.display(description='Изображение_5')
    def post_image5(self, Product):
        if Product.image5:
            return mark_safe(f"<img src='{Product.image1.url}' width=75>")
        return 'Нет фото'



class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


