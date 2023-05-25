# Generated by Django 4.0 on 2023-04-13 18:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_customuser_role_alter_computers_arrival_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 13, 18, 28, 47, 628050, tzinfo=utc), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='position',
            field=models.CharField(max_length=200, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 13, 18, 28, 47, 628050, tzinfo=utc), verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='sys_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sys_id', to='api.emp', unique=True, verbose_name='Сисадмин'),
        ),
    ]