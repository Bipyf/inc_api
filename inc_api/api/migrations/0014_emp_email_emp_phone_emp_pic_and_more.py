# Generated by Django 4.0 on 2023-05-03 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_computers_arrival_date_alter_computers_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='emp',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='emp',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='pfp'),
        ),
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 5, 4), verbose_name='Дата прибытия'),
        ),
    ]
