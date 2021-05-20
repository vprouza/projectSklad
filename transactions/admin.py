from django.contrib import admin

from .models import Transaction, Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'total_price', 'date_created')
    search_fields = ['id']

admin.site.register(Transaction)
admin.site.register(Order, OrderAdmin)