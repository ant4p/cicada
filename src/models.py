from django.db import models


class IndexVideo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', default='Видео(главная страница)')
    video = models.FileField(upload_to='videos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Видео на главной странице' )

    class Meta:
        db_table = 'title_video'
        verbose_name = 'Видео(главная страница)'
        verbose_name_plural = 'Видео(главная страница)'

    def __str__(self):
        return self.title



class UserAgreement(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', default='Пользовательское соглашение')
    content = models.TextField(blank=True, verbose_name='Текст соглашения')

    class Meta:
        db_table = 'agreement'
        verbose_name = 'Пользовательское соглашение'
        verbose_name_plural = 'Пользовательское соглашение'

    def __str__(self):
        return self.title

class TitleImageCooperation(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок', default='Титульное изображение(блок сотрудничество)')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Титульное изображение (Абстракция Высокое_качество)')

    class Meta:
        db_table = 'title_image_cooperation'
        verbose_name = 'Титульное изображение(блок сотрудничество)'
        verbose_name_plural = 'Титульное изображение(блок сотрудничество)'

    def __str__(self):
        return self.title

class CaseCooperation(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', default='Кейс(блок сотрудничество)')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, null=True, blank=True, verbose_name='Титульное изображение (Квадрат min_420x420px)')
    title_case = models.CharField(max_length=100, verbose_name='Заголовок кейса', default='Кейс: Создание детских игрушек')
    title_task = models.CharField(max_length=100, verbose_name='Заголовок блока задача',default='Задача клиента:')
    text_task = models.TextField(blank=True, verbose_name='Текст блока задача')
    title_solution = models.CharField(max_length=100, verbose_name='Заголовок блока решение', default='Решение от мастерской 3D CICADA')
    text_solution = models.TextField(blank=True, verbose_name='Текст блока решение')
    title_result = models.CharField(max_length=100, verbose_name='Заголовок блока результат', default='Результат:')
    text_result = models.TextField(blank=True, verbose_name='Текст блока результат')

    class Meta:
        db_table = 'case_cooperation'
        verbose_name = 'Кейс(блок сотрудничество)'
        verbose_name_plural = 'Кейс(блок сотрудничество)'

    def __str__(self):
        return self.title