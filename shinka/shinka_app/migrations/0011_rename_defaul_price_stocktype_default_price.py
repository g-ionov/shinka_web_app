# Generated by Django 4.0.2 on 2022-02-27 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shinka_app', '0010_remove_history_service_remove_history_stock_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocktype',
            old_name='defaul_price',
            new_name='default_price',
        ),
    ]
