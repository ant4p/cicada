from django.db import models


class UserAgreement(models.Model):
    content = models.TextField(blank=True, verbose_name='Текст соглашения')

    class Meta:
        db_table = 'agreement'
        verbose_name = 'Пользовательское соглашение'
        verbose_name_plural = 'Пользовательское соглашение'
