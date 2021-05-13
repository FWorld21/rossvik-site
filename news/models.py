from django.db import models
from django.urls import reverse
from rossvik.translator import translate


# Create your models here.
class News(models.Model):
    image = models.ImageField(upload_to='media', verbose_name='Главная картинка', blank=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок', unique=True)
    slug = models.CharField(max_length=100, blank=True)
    timestamp = models.DateField(auto_now_add=False, verbose_name='Дата', editable=True, blank=False)
    author_name = models.CharField(max_length=50, verbose_name='Имя автора')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_url(self):
        return reverse('news_card_ru', args=[f'{self.slug}'])

    def get_url_uz(self):
        return reverse('news_card_uz', args=[f'{self.slug}'])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if True:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Для новости', default=None)
    image = models.ImageField(upload_to='media', verbose_name='Фото')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Comments(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='Для новости', default=None)
    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    author_mail = models.CharField(max_length=200, verbose_name='Почта автора')
    site = models.CharField(max_length=100, verbose_name='Сайт автора', blank=True)
    comment = models.TextField(verbose_name='Коментарий')
    post = models.BooleanField(verbose_name='Опубликовать?', blank=False)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return f'Прокоментировал {self.author_name} к новости {self.news.title}'
