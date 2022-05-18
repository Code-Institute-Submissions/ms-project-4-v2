from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """ Customised admin to add fields """
    list_display = (
        'name',
        'friendly_name',
    )


class ProductAdmin(admin.ModelAdmin):
    """ Customised admin to add fields """
    list_display = (
        'name',
        'category',
        'description',
        'price',
        'image',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
