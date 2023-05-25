# Generated by Django 4.0 on 2023-05-15 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_computers_arrival_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='tsk_acc_date',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='tsk_cmp_date',
        ),
        migrations.AddField(
            model_name='tasks',
            name='tsk_dedl_date',
            field=models.DateTimeField(blank=True, default='2023-05-15 17:49', null=True, verbose_name='Дата дедлайна'),
        ),
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 5, 15), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateTimeField(blank=True, default='2023-05-15 17:49', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_acc_date',
            field=models.DateTimeField(blank=True, default='2023-05-15 17:49', null=True, verbose_name='Дата принятия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_cmp_date',
            field=models.DateTimeField(blank=True, default='2023-05-15 17:49', null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='reg_date',
            field=models.DateTimeField(blank=True, default='2023-05-15 17:49', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='tsk_status',
            field=models.CharField(choices=[('Невыполнено', 'Невыполнено'), ('Выполнено', 'Выполнено')], max_length=200, verbose_name='Статус'),
        ),
    ]