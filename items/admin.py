from django.contrib import admin
from django.db import models
from .models import Item, Category, SubCategory, Supplier


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'supplier', 'price', 'date_modified')
    search_fields = ['name', 'description']
    list_filter = ('supplier','category', 'subcategory')
    filter_horizontal = ('subcategory',)

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Supplier)

