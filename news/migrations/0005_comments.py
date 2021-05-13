# Generated by Django 3.2.1 on 2021-05-06 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_images_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('author_mail', models.CharField(max_length=200, verbose_name='Почта автора')),
                ('site', models.CharField(blank=True, max_length=100, verbose_name='Сайт автора')),
                ('comment', models.TextField(verbose_name='Коментарий')),
                ('post', models.BooleanField(verbose_name='Опубликовать?')),
                ('news', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Для новости')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
