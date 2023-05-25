# Generated by Django 4.0 on 2023-04-15 11:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_computers_arrival_date_alter_customuser_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 15, 11, 0, 3, 470641, tzinfo=utc), verbose_name='Дата прибытия'),
        ),
    ]
