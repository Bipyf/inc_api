# Generated by Django 4.0 on 2023-02-04 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customuser_role_alter_computers_arrival_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 4, 14, 49, 13, 101323, tzinfo=utc), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 4, 14, 49, 13, 101323, tzinfo=utc), verbose_name='Дата регистрации'),
        ),
    ]
