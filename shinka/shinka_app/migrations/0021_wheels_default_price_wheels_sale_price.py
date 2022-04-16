# Generated by Django 4.0.2 on 2022-03-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinka_app', '0020_remove_wheels_work_wheels_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='wheels',
            name='default_price',
            field=models.IntegerField(default=100, verbose_name='Закупочная цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wheels',
            name='sale_price',
            field=models.IntegerField(default=200, verbose_name='Стоимость продажи'),
            preserve_default=False,
        ),
    ]