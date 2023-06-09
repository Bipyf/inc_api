# Generated by Django 4.0 on 2023-03-02 12:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_computers_arrival_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairrequests',
            name='sys_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sys_id', to='api.emp', unique=True, verbose_name='Сотрудник'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 2, 12, 24, 34, 400980, tzinfo=utc), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_id', to='api.emp', unique=True, verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 3, 2, 12, 24, 34, 401977, tzinfo=utc), verbose_name='Дата регистрации'),
        ),
    ]
