from django.contrib import admin

from tags.models import Tag


class TagAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
    ]
    readonly_fields = [
        'slug',
    ]

    list_display = ('title', )
    list_display_links = ('title', )
    list_per_page = 15
    search_fields = ['title', ]
    save_on_top = True

admin.site.register(Tag, TagAdmin)
