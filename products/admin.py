from django.contrib import admin

from products.models import ProductCategory, Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)


