from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
    ]
    prepopulated_fields = {'slug': ('title', )}

    list_display = ('title', )
    list_display_links = ('title', )
    save_on_top = True

admin.site.register(Tag, TagAdmin)
