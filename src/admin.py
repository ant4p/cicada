from django.contrib import admin

from src.models import UserAgreement


class UserAgreementAdmin(admin.ModelAdmin):
    fields = ['content']

admin.site.register(UserAgreement, UserAgreementAdmin)
