from django.db import models


class About(models.Model):
    text = models.TextField(verbose_name='текст')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return 'О нас'
