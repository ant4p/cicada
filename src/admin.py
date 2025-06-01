from django.contrib import admin
from django.utils.safestring import mark_safe

from src.models import UserAgreement, TitleImageCooperation, CaseCooperation, IndexVideo, Contacts


class ContactsAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'whatsapp_title',
        'whatsapp_url',
        'telegram_title',
        'telegram_url',
        'phone_title',
        'phone_url',
        'email_title',
        'email_url',
        'vk_title',
        'vk_url',
    ]

    list_display = ( 'title', 'whatsapp_url', 'telegram_url', 'phone_url', 'email_url', 'vk_url', )
    readonly_fields = ('title', )

class IndexVideoAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'video',
    ]

    list_display = ('title', )
    readonly_fields = ('title',)

class UserAgreementAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'content',
    ]
    readonly_fields = ('title',)

class TitleImageCooperationAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'title_image',
        'post_title_image_cooperation',
    ]
    readonly_fields = [
        'title',
        'post_title_image_cooperation',
    ]
    list_display = ('title', 'post_title_image_cooperation', )

    @admin.display(description='Титульное изображение')
    def post_title_image_cooperation(self, TitleImageCooperation):
        if TitleImageCooperation.title_image:
            return mark_safe(f"<img src='{TitleImageCooperation.title_image.url}' width=75>")
        return 'Нет фото'


class CaseCooperationAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'title_image',
        'post_image_case_cooperation',
        'title_case',
        'title_task',
        'text_task',
        'title_solution',
        'text_solution',
        'title_result',
        'text_result',
    ]
    readonly_fields = [
        'title',
        'post_image_case_cooperation',
    ]
    list_display = ('title', 'post_image_case_cooperation', )

    @admin.display(description='Титульное изображение')
    def post_image_case_cooperation(self, CaseCooperation):
        if CaseCooperation.title_image:
            return mark_safe(f"<img src='{CaseCooperation.title_image.url}' width=75>")
        return 'Нет фото'

admin.site.register(UserAgreement, UserAgreementAdmin)
admin.site.register(TitleImageCooperation, TitleImageCooperationAdmin)
admin.site.register(CaseCooperation, CaseCooperationAdmin)
admin.site.register(IndexVideo, IndexVideoAdmin)
admin.site.register(Contacts, ContactsAdmin)
