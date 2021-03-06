# Generated by Django 3.1.6 on 2021-04-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20210415_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='date changed'),
        ),
    ]
