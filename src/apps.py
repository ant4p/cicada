from django.apps import AppConfig


class SrcConfig(AppConfig):
    verbose_name = 'Общие настройки сайта'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src'
