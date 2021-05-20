from django.db import models
from django.contrib.auth.models import User
from transactions.models import Order

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    order_in_progress = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, default=None)
