from django.contrib import admin
from django.db import models
from .models import Item, ItemAdmin, Category


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
#admin.site.register(ItemAdmin)

