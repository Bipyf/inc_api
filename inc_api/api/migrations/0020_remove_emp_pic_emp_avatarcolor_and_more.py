# Generated by Django 4.0 on 2023-05-07 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_repairrequests_reg_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='pic',
        ),
        migrations.AddField(
            model_name='emp',
            name='avatarColor',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 5, 8), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateTimeField(blank=True, default='2023-05-08 05:13', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_acc_date',
            field=models.DateTimeField(blank=True, default='2023-05-08 05:13', null=True, verbose_name='Дата принятия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_cmp_date',
            field=models.DateTimeField(blank=True, default='2023-05-08 05:13', null=True, verbose_name='Дата выполнения'),
        ),
    ]
