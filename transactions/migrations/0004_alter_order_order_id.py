# Generated by Django 3.2.2 on 2021-05-20 16:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20210520_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='order id'),
        ),
    ]
