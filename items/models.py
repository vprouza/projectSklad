from django.contrib import admin
from django.db import models
import datetime
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("name of category"), max_length=255)
    description = models.TextField(_("description"),default="", blank=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(_("name of subcategory"), max_length=255)
    description = models.TextField(_("description"),default="", blank=True)
    parent = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("subcategory")
        verbose_name_plural = _("subcategories")
    def __str__(self):
        return (self.parent.__str__() + " - " + self.name)

class Supplier(models.Model):
    name = models.CharField(_("name of supplier"), max_length=255)
    description = models.TextField(_("description"),default="", blank=True)
    link = models.URLField(_("url"),default="", blank=True)

    class Meta:
        verbose_name = _("supplier")
        verbose_name_plural = _("suppliers")
    def __str__(self):
        return self.name

class Item(models.Model):
    UNITS = [
    ('m', _("metres")),
    ('pcs', _("pieces")),
    ('cm', _("centimetres")),
    ]
    name = models.CharField(_("name"),max_length=255)
    description = models.TextField(_("description"),default="", blank=True)
    count = models.IntegerField(_("count"),default=0)
    supplier = models.ForeignKey(Supplier, verbose_name=_("supplier"), on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.CharField(_("unit"),choices=UNITS, max_length=4, default="pcs")
    price = models.DecimalField(_("price per unit"),default=0,decimal_places=2,max_digits=10)
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ManyToManyField(SubCategory, verbose_name=_("subcategories"), blank=True)
    date_added = models.DateTimeField(_("date created"),auto_now_add=True)
    date_modified = models.DateTimeField(_("date changed"),auto_now=True)

    class Meta:
        verbose_name = _("item")
        verbose_name_plural = _("items")
    def __str__(self):
        return self.name
