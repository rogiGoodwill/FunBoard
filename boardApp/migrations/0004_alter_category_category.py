# Generated by Django 4.1.3 on 2022-12-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardApp', '0003_alter_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('Танки', 'Танки'), ('Хиллы', 'Хиллы'), ('DD', 'DD'), ('Торговцы', 'Торговцы'), ('Гилдмастеры', 'Гилдмастеры'), ('Квестгиверы', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), ('Кожевники', 'Кожевники'), ('Зельевары', 'Зельевары'), ('Мастеры заклинаний', 'Мастеры заклинаний')], default='Танки', max_length=18),
        ),
    ]