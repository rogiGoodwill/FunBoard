from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
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
        (spellMaster, 'Мастеры заклинаний')
    ]

    category = models.CharField(max_length=3, choices=CATEGORIES)


class Ad(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    picture = models.ImageField()
    videoLink = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comments(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    comment = models.TextField()
