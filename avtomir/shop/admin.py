from django.contrib import admin
from .models import Products
from import_export.admin import ImportExportModelAdmin


class ProductAdmin(ImportExportModelAdmin):
    pass
admin.site.register(Products, ProductAdmin)
