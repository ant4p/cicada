from django.db import models


class Contacts(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, default='Контакты', verbose_name='Контакты')
    whatsapp_title = models.CharField(max_length=50, blank=True, null=True, default='Whatsapp', verbose_name='Whatsapp')
    whatsapp_url = models.URLField(max_length=200, blank=True, null=True, default='', verbose_name='Ссылка на чат в Whatsapp - https://wa.me/7__________')
    telegram_title = models.CharField(max_length=50, blank=True, null=True, default='Telegram', verbose_name='Telegram')
    telegram_url = models.URLField(max_length=200, blank=True, null=True, default='', verbose_name='Ссылка на чат в Telegram - https://t.me/______')
    phone_title = models.CharField(max_length=50, blank=True, null=True, default='+7-___-___-__-__', verbose_name='Номер телефона - +7__________')
    phone_url = models.CharField(max_length=200, blank=True, null=True, default='',
                            verbose_name='Ссылка звонок на указанный номер телефона')
    email_title = models.CharField(max_length=50, blank=True, null=True, default='___@mail.ru', verbose_name='Электронная почта - ____@___.__')
    email_url = models.CharField(max_length=200, blank=True, null=True, default='',
                            verbose_name='Ссылка на электронную почту')
    vk_title = models.CharField(max_length=50, blank=True, null=True, default='Вконтакте', verbose_name='Вконтакте')
    vk_url = models.URLField(max_length=200, blank=True, null=True, default='', verbose_name='Ссылка на группу Вконтакте - https://vk.com/______')

    class Meta:
        db_table = 'contacts'
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.title

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
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d',
                                    default=None, null=True, blank=True,
                                    verbose_name='Титульное изображение (Абстракция Высокое_качество)'
                                                 'загружать сразу оптимизированное - размер до 300Кб')

    class Meta:
        db_table = 'title_image_cooperation'
        verbose_name = 'Титульное изображение(блок сотрудничество)'
        verbose_name_plural = 'Титульное изображение(блок сотрудничество)'

    def __str__(self):
        return self.title

class CaseCooperation(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', default='Кейс(блок сотрудничество)')
    title_image = models.ImageField(upload_to='photos/%Y/%m/%d',
                                    default=None, null=True, blank=True,
                                    verbose_name='Титульное изображение (Квадрат min_420x420px)'
                                                 'или прямоугольник(ширина больше высоты)'
                                                 'загружать сразу оптимизированное - размер до 300Кб')
    title_case = models.CharField(max_length=100, verbose_name='Заголовок кейса', default='Кейс: Создание детских игрушек')
    title_task = models.CharField(max_length=100, verbose_name='Заголовок блока задача',default='Задача клиента:')
    text_task = models.TextField(blank=True, verbose_name='Текст блока задача')
    title_solution = models.CharField(max_length=100, verbose_name='Заголовок блока решение', default='Решение от 3D мастерской  MOSPRINT')
    text_solution = models.TextField(blank=True, verbose_name='Текст блока решение')
    title_result = models.CharField(max_length=100, verbose_name='Заголовок блока результат', default='Результат:')
    text_result = models.TextField(blank=True, verbose_name='Текст блока результат')

    class Meta:
        db_table = 'case_cooperation'
        verbose_name = 'Кейс(блок сотрудничество)'
        verbose_name_plural = 'Кейс(блок сотрудничество)'

    def __str__(self):
        return self.title