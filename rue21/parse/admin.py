from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product
from .resources import ProductResource

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('po', 'item', 'color', 'size', 'description', 'qty')
