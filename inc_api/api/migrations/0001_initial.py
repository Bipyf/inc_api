# Generated by Django 4.0 on 2023-02-01 17:35

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=200, null=True, verbose_name='Имя оборудования')),
                ('condition', models.CharField(choices=[('Свободное', 'Свободное'), ('На рабочем месте', 'На рабочем месте'), ('В ремонте', 'В ремонте'), ('Снято с учета', 'Снято с учета')], max_length=200, verbose_name='Состояние')),
                ('arrival_date', models.DateField(blank=True, default=datetime.datetime(2023, 2, 1, 17, 35, 5, 105256, tzinfo=utc), verbose_name='Дата прибытия')),
                ('deletion_date', models.DateField(blank=True, null=True, verbose_name='Дата снятия')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Заметки')),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('lastname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=200, unique=True, verbose_name='Должность')),
            ],
        ),
        migrations.CreateModel(
            name='Work_Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace_name', models.CharField(max_length=200, verbose_name='Название отдела')),
                ('cabinet', models.CharField(max_length=200, verbose_name='Кабинет/цех')),
            ],
        ),
        migrations.CreateModel(
            name='RepairRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(blank=True, default=datetime.datetime(2023, 2, 1, 17, 35, 5, 106253, tzinfo=utc), verbose_name='Дата регистрации')),
                ('req_desc', models.TextField(verbose_name='Содержание')),
                ('req_status', models.CharField(choices=[('Принято', 'Принято'), ('В процессе', 'В процессе'), ('Выполнено', 'Выполнено')], max_length=200, verbose_name='Статус')),
                ('req_acc_date', models.DateField(blank=True, null=True, verbose_name='Дата принятия')),
                ('req_cmp_date', models.DateField(blank=True, null=True, verbose_name='Дата выполнения')),
                ('computer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.computers', verbose_name='ID компьютера')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.emp', verbose_name='Сотрудник')),
            ],
        ),
        migrations.AddField(
            model_name='emp',
            name='position',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='api.position', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='emp',
            name='workplace_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.work_catalogue', verbose_name='Место работы'),
        ),
        migrations.AddField(
            model_name='computers',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.emp'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
