from django.contrib import admin
from django.db import models
from .models import Item, ItemAdmin, Category, SubCategory, Supplier


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Supplier)
#admin.site.register(ItemAdmin)

