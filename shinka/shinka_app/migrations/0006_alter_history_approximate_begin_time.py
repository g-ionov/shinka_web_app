# Generated by Django 4.0.2 on 2022-02-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinka_app', '0005_alter_history_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='approximate_begin_time',
            field=models.TimeField(verbose_name='Предположительное время начала работы'),
        ),
    ]
