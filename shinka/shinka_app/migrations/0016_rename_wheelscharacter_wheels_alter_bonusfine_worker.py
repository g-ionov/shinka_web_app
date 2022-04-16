# Generated by Django 4.0.2 on 2022-03-10 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shinka_app', '0015_alter_servicework_options_alter_stock_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WheelsCharacter',
            new_name='Wheels',
        ),
        migrations.AlterField(
            model_name='bonusfine',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shinka_app.worker', verbose_name='Рабочий'),
        ),
    ]