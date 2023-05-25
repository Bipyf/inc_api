from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
import datetime

STAT_CHOICES = (
    ("Принято", "Принято"),
    ("В процессе", "В процессе"),
    ("Выполнено", "Выполнено"),
)
STATS_CHOICES = (
    ("Невыполнено", "Невыполнено"),
    ("Выполнено", "Выполнено"),
)
COMP_CHOICES = (
    ("Свободное", "Свободное"),
    ("На рабочем месте", "На рабочем месте"),
    ("В ремонте", "В ремонте"),
    ("Снято с учета", "Снято с учета"),
)
class Position(models.Model):
    pos = models.CharField(verbose_name="Должность", max_length=200, unique=True)
    def __str__(self):
        return  str(self.pos) 

class Work_Catalogue(models.Model):
    workplace_name = models.CharField(max_length=200, verbose_name="Название отдела")
    cabinet = models.CharField(max_length=200, verbose_name="Кабинет/цех")
    def __str__(self):
        return self.workplace_name + ' (id: ' + str(self.id) + ')'
class Emp(models.Model):
    workplace_id = models.ForeignKey( Work_Catalogue, blank=True, null=True, to_field='id', on_delete=models.CASCADE, verbose_name="Место работы")
    name = models.CharField(max_length=200, verbose_name="Имя")
    surname = models.CharField(max_length=200, verbose_name="Фамилия")
    lastname = models.CharField(max_length=200, blank=True, null=True, verbose_name="Отчество")
    position = models.CharField(max_length=200, verbose_name="Должность")
    phone = models.CharField(max_length=200, verbose_name="Телефон", blank=True, null=True,)
    email = models.CharField(max_length=200, verbose_name="Email", blank=True, null=True,)
    avatarColor = models.CharField(max_length=200, verbose_name="Цвет", blank=True, null=True,)
    def __str__(self):
        return self.name + ' ' + self.surname + ' (id: ' + str(self.id) + ')'
    

class Computers(models.Model):
    device_name = models.CharField( null=True, max_length=200, verbose_name="Имя оборудования")
    condition = models.CharField(max_length=200, verbose_name="Состояние", choices=COMP_CHOICES)
    arrival_date = models.DateField(default=datetime.date.today(), verbose_name="Дата прибытия",  blank=True)
    deletion_date = models.DateField(blank=True, null=True, verbose_name="Дата снятия")
    notes = models.TextField(blank=True, null=True,verbose_name="Заметки")
    owner = models.ForeignKey(Emp, to_field="id", on_delete=models.CASCADE, blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.condition == "Снято с учета":
            self.deletion_date = datetime.date.today().strftime("%Y-%m-%d")
              
        super(Computers, self).save(*args, **kwargs)

    def __str__(self):
       return self.device_name + " "  + ' (id: ' + str(self.id) + ')'
        
class RepairRequests(models.Model):
    emp_id = models.ForeignKey(Emp, to_field='id', on_delete=models.CASCADE, verbose_name="Сотрудник", related_name="emp_id", blank=True, null=True)
    computer = models.ForeignKey(Computers,blank=True, null=True, to_field='id', on_delete=models.CASCADE, verbose_name="ID компьютера" )
    reg_date = models.DateTimeField(verbose_name="Дата регистрации", default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),blank=True)
    req_desc = models.TextField( verbose_name="Содержание")
    req_status = models.CharField(max_length=200, verbose_name="Статус", choices=STAT_CHOICES)
    req_acc_date = models.DateTimeField( blank=True, null=True, verbose_name="Дата принятия")
    req_cmp_date = models.DateTimeField( blank=True, null=True, verbose_name="Дата выполнения")
    sys_id = models.ForeignKey(Emp, to_field='id', on_delete=models.CASCADE, verbose_name="Сисадмин", unique=False, related_name="sys_id", blank=True, null=True,)
    def save(self, *args, **kwargs):
        if self.req_status == "В процессе":
         if self.computer is not None:
             cond = Computers.objects.get(id = self.computer.id)
             cond.condition="В ремонте"
             cond.save()
         self.req_acc_date= datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        elif self.req_status == "Выполнено":
         if self.computer is not None:
             cond = Computers.objects.get(id = self.computer.id)
             cond.condition="На рабочем месте"
             cond.save()
         self.req_cmp_date= datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        super(RepairRequests, self).save(*args, **kwargs)
    def __str__(self):
        return 'Заявка №' +  str(self.id) 

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    ROLE_CHOICES = (
        ('Админ', 'Админ'),
        ('Сотрудник', 'Сотрудник'),
        ('Сисадмин', 'Сисадмин'),
        ('HR', 'HR'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="Employee"
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='O',
    )
    surname = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
class Tasks(models.Model):
    emp_id = models.ForeignKey(Emp, to_field='id', on_delete=models.CASCADE, verbose_name="Сотрудник", related_name="empl_id", blank=True, null=True)
    reg_date = models.DateTimeField(verbose_name="Дата регистрации", default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),blank=True)
    tsk_desc = models.TextField( verbose_name="Содержание")
    tsk_status = models.CharField(max_length=200, verbose_name="Статус", choices=STATS_CHOICES)
    tsk_dedl_date = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M'), blank=True, null=True, verbose_name="Дата дедлайна")
    hr_id = models.ForeignKey(Emp, to_field='id', on_delete=models.CASCADE, verbose_name="Руководитель", unique=False, related_name="hr_id", blank=True, null=True,)

@receiver(models.signals.post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    if created:
          emp = Emp.objects.create(id = instance.id ,name = instance.first_name, surname = instance.last_name, lastname = instance.surname, position = instance.role, email=instance.email, phone=instance.phone)
