# Generated by Django 4.0 on 2023-05-12 12:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_remove_emp_pic_emp_avatarcolor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='arrival_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 5, 12), verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='reg_date',
            field=models.DateTimeField(blank=True, default='2023-05-12 18:28', verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_acc_date',
            field=models.DateTimeField(blank=True, default='2023-05-12 18:28', null=True, verbose_name='Дата принятия'),
        ),
        migrations.AlterField(
            model_name='repairrequests',
            name='req_cmp_date',
            field=models.DateTimeField(blank=True, default='2023-05-12 18:28', null=True, verbose_name='Дата выполнения'),
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(blank=True, default='2023-05-12 18:28', verbose_name='Дата регистрации')),
                ('tsk_desc', models.TextField(verbose_name='Содержание')),
                ('tsk_status', models.CharField(choices=[('Принято', 'Принято'), ('В процессе', 'В процессе'), ('Выполнено', 'Выполнено')], max_length=200, verbose_name='Статус')),
                ('tsk_acc_date', models.DateTimeField(blank=True, default='2023-05-12 18:28', null=True, verbose_name='Дата принятия')),
                ('tsk_cmp_date', models.DateTimeField(blank=True, default='2023-05-12 18:28', null=True, verbose_name='Дата выполнения')),
                ('emp_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empl_id', to='api.emp', verbose_name='Сотрудник')),
                ('hr_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hr_id', to='api.emp', verbose_name='Руководитель')),
            ],
        ),
    ]