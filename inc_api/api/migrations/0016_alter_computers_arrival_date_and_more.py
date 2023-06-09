# Generated by Django 4.0 on 2023-05-07 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_computers_arrival_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 5, 7), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateTimeField(blank=True, default='2023-05-07 22:52', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_acc_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата принятия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_cmp_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
