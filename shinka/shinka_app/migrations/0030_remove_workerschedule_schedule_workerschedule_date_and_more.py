# Generated by Django 4.0.2 on 2022-03-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shinka_app', '0029_workerschedule_hours_workerschedule_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerschedule',
            name='schedule',
        ),
        migrations.AddField(
            model_name='workerschedule',
            name='date',
            field=models.DateField(default='2022-03-23', verbose_name='Дата работы'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
