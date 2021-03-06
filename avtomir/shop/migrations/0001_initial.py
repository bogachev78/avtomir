# Generated by Django 3.1.3 on 2020-11-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=150, verbose_name='Ценник')),
                ('catalog_number', models.CharField(max_length=50, verbose_name='№ каталога')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('ostatok', models.CharField(max_length=50, verbose_name='Остаток')),
                ('edizm', models.CharField(max_length=10, verbose_name='Ед.изм')),
            ],
        ),
    ]
