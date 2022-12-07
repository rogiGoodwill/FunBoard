from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# class Category(models.Model):
#     tanks = 'TNK'
#     hills = 'HIL'
#     DD = 'DD'
#     dealers = 'DLR'
#     gildmasters = 'GMR'
#     questgivers = 'QGR'
#     blacksmith = 'BST'
#     tanner = 'TNR'
#     potionMaster = 'PMR'
#     spellMaster = 'SMR'
#
#     CATEGORIES = [
#         (tanks, 'Танки'),
#         (hills, 'Хиллы'),
#         (DD, 'DD'),
#         (dealers, 'Торговцы'),
#         (gildmasters, 'Гилдмастеры'),
#         (questgivers, 'Квестгиверы'),
#         (blacksmith, 'Кузнецы'),
#         (tanner, 'Кожевники'),
#         (potionMaster, 'Зельевары'),
#         (spellMaster, 'Мастеры заклинаний')
#     ]
#
#     category = models.CharField(max_length=3, choices=CATEGORIES)


class Ad(models.Model):
    tanks = 'TNK'
    hills = 'HIL'
    DD = 'DD'
    dealers = 'DLR'
    gildmasters = 'GMR'
    questgivers = 'QGR'
    blacksmith = 'BST'
    tanner = 'TNR'
    potionMaster = 'PMR'
    spellMaster = 'SMR'

    CATEGORIES = [
        (tanks, 'Танки'),
        (hills, 'Хиллы'),
        (DD, 'DD'),
        (dealers, 'Торговцы'),
        (gildmasters, 'Гилдмастеры'),
        (questgivers, 'Квестгиверы'),
        (blacksmith, 'Кузнецы'),
        (tanner, 'Кожевники'),
        (potionMaster, 'Зельевары'),
        (spellMaster, 'Мастеры заклинаний')]


    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    picture = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    videoLink = models.CharField(max_length=255, verbose_name='Ссылка на видео', blank=True, null=True)
    category = models.CharField(max_length=3, choices=CATEGORIES, verbose_name='Категории', blank=False, default='TNK', null=False)


class Comments(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    comment = models.TextField()
