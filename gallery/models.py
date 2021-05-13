from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=120, verbose_name='Заголовок')
    timestamp = models.DateField(auto_now_add=False, verbose_name='Дата', editable=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Для заголовка', default=None)
    image = models.ImageField(upload_to='media', verbose_name='Фото', blank=False)

    def __str__(self):
        return self.post.name

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

