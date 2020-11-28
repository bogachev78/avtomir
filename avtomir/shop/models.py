from django.db import models

class Products(models.Model):
    number = models.CharField(max_length=150, verbose_name='Ценник', db_index=True)
    catalog_number = models.CharField(max_length=50, verbose_name='№ каталога', db_index=True)
    title = models.CharField(max_length=255, verbose_name='Наименование', db_index=True)
    price = models.CharField(max_length=50, verbose_name='Цена', db_index=True)
    ostatok = models.CharField(max_length=50, verbose_name='Остаток', db_index=True)
    edizm = models.CharField(max_length=10, verbose_name='Ед.изм', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
