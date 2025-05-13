from django.contrib import admin

from services.models import Service, ServiceItem


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ServiceItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
