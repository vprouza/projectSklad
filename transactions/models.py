from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


from items.models import Item
# Create your models here.

class Order(models.Model):
    order_id = models.UUIDField(_("order id"),default=uuid.uuid4)
    date_created = models.DateTimeField(_("date created"),auto_now_add=True)
    discount = models.IntegerField(_("discount"), default=0)
    total_price = models.DecimalField(_("total price"),default=0,decimal_places=2,max_digits=10)

    def short_id(self):
        return str(self.order_id)[-6:]

    def __str__(self):
        return self.short_id()

class Transaction(models.Model):
    item = models.ForeignKey(Item, verbose_name=_("item"), on_delete=models.PROTECT)
    amount = models.DecimalField(_("amount"),decimal_places=2,max_digits=10)
    price = models.DecimalField(_("price per unit"),default=0,decimal_places=2,max_digits=10)
    STATUS = [
    ('res',_("reserved")),
    ('fin',_("finished")),
    ]
    STATUS = models.CharField(_("status"),choices=STATUS, max_length=3, default="res")
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.PROTECT, null=True)