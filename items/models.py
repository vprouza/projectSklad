from django.contrib import admin
from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(_("name of category"), max_length=255)
    description = models.TextField(_("description"),default="")

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
    def __str__(self):
        return self.name

class Item(models.Model):
    #list_display('name','count')
    UNITS = [
    ('m', _("metres")),
    ('pcs', _("pieces")),
    ('cm', _("centimetres")),
    ]
    name = models.CharField(_("name"),max_length=255)
    count = models.IntegerField(_("count"),default=0)
    unit = models.CharField(_("unit"),choices=UNITS, max_length=4, default="pcs")
    price = models.DecimalField(_("price per unit"),default=0,decimal_places=2,max_digits=10)
    category = models.ManyToManyField(Category, verbose_name=_("categories"))
    date_added = models.DateTimeField(_("date created"),auto_now_add=True)
    date_modified = models.DateTimeField(_("date changed"),auto_now=True)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
    def __str__(self):
        return self.name

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'price', 'date_modified')