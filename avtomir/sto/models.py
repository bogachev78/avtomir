from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Plus(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(max_length=255, verbose_name='Содержание', )
    active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
    

class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')
    photo = models.ImageField(upload_to='media/service/', verbose_name='Фото', blank=True)
    body = RichTextUploadingField()
    active = models.BooleanField(default=True, verbose_name='Активно')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'



class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')
    photo = models.ImageField(upload_to='media/blog/', verbose_name='Фото', blank=True)
    body = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Contact(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phone = models.CharField(max_length=255, verbose_name='Телефон')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Paz(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = RichTextUploadingField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис ПАЗ'
        verbose_name_plural = 'Сервисы ПАЗ'