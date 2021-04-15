# Generated by Django 3.1.6 on 2021-02-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cena za jednotku'),
        ),
    ]
