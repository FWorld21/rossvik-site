from django.db import models
from rossvik.translator import translate
from django.shortcuts import reverse


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media',  default='')

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.name)
        super().save(*args, **kwargs)


class SubCategories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название подкатегории')
    slug = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='media',  default='')
    category = models.ForeignKey(Categories, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Подкатегорию'
        verbose_name_plural = 'Подкатегории'

    def get_url(self):
        return reverse('items_ru', args=[f'{self.slug}'])

    def get_url_uz(self):
        return reverse('items_uz', args=[f'{self.slug}'])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    slug = models.CharField(max_length=100, blank=True)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Цена товара')
    image = models.ImageField(upload_to='media', verbose_name='Фотография товара')
    description = models.TextField(verbose_name='Описание товара')
    article = models.CharField(max_length=20, verbose_name='Артикул')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_url(self):
        return reverse('product_card_ru', args=[f'{self.slug}'])

    def get_url_uz(self):
        return reverse('product_card_uz', args=[f'{self.slug}'])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.name)
        super().save(*args, **kwargs)
