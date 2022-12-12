from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     profile = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    """
    Модель категорий
    """

    category = models.CharField(max_length=18, blank=False, null=False)

    def __str__(self):
        return self.category


class Ad(models.Model):
    """
    Модель объявлений
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    picture = models.ImageField(verbose_name='Изображение', blank=True, null=True, upload_to='media')
    videoLink = models.CharField(max_length=255, verbose_name='Ссылка на видео', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории', blank=False,
                                 null=False)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def get_absolute_url(self):
        return f'ad/{self.pk}'

    def __str__(self):
        return self.text[:20] + '...'


class Comments(models.Model):
    """
    Модель комментариев
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    comment = models.TextField(verbose_name='Комментарий')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')


    def __str__(self):
        return self.comment[:20]+' ...'

