import io
from .models import RepairRequests, Emp
import operator
import xlsxwriter
from datetime import datetime
from django.utils.translation import gettext
from statistics import  mean

format = '%Y-%m-%d %H:%M'

class ForExc():
   id = 0
   count = 0
   countsuc = 0
   avg = []
   aver = 0.0
   eff = 0.0
   def __init__(self,id):
       self.id = id
       self.avg = []



def WriteToExcel():
    my_dict = {}
    datareq = RepairRequests.objects.all()
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_a = workbook.add_worksheet("Анализ успешности (SYS)")
    worksheet_b = workbook.add_worksheet("Анализ запросов")
    worksheet_c = workbook.add_worksheet("Анализ успешности")
    bar_chart = workbook.add_chart({"type": "column"})
    merged_format = workbook.add_format(
        {
      
        "bold": 1,
        "border": 1,
        "align": "center",
        "valign": "vcenter",
        "bg_color":"#D3D3D3"
        }
    
    )
    header_format = workbook.add_format(
        {
         
        "bold": 1,
        "border": 1,
        "align": "center",
        }
    )
    data_format = workbook.add_format(
        {
           
        
        "border": 1,
        "align": "center",
        }
    )
    eff_format = workbook.add_format(
        {
           
        "bg_color":"#90EE90",
        "border": 1,
        "align": "center",
        }
    )
    percent_format = workbook.add_format({"num_format": "0%", "border":1})
    worksheet_a.set_column(0,6, 20)
    for data in datareq:
     
     if  data.req_status=="Выполнено":
        key = data.sys_id
        
        if my_dict.get(key)!=None:
            my_dict[key].countsuc+=1
            my_dict[key].count+=1
            c = str(data.req_cmp_date).replace(':00+00:00', '')
            C = datetime.strptime(c, format)
            b = str(data.req_acc_date).replace(':00+00:00', '')
            B = datetime.strptime(b, format)
            diff = C - B
            my_dict[key].avg.append(int(diff.total_seconds()/3600))
        
            
        else:
           my_dict[key] = ForExc(id=key)
           my_dict[key].countsuc+=1
           my_dict[key].count+=1
           c = str(data.req_cmp_date).replace(':00+00:00', '')
           C = datetime.strptime(c, format)
           b = str(data.req_acc_date).replace(':00+00:00', '')
           B = datetime.strptime(b, format)
           diff = C - B
           
           my_dict[key].avg.append(int(diff.total_seconds()/3600))
           
     elif data.req_status=="В процессе":
        key =data.sys_id
        if my_dict.get(key)!=None:
            my_dict[key].count+=1
        else:
           my_dict[key] = ForExc(id=key)
   
    worksheet_a.merge_range(0, 0, 0, 5, "Анализ успешности сисадминов", merged_format)
    worksheet_a.write(1, 0, "Имя",  header_format)
    worksheet_a.write(1, 1, "Количество заявок",  header_format)
    worksheet_a.write(1, 2, "Количество выполненных",  header_format)
    worksheet_a.write(1, 3, "Процент выполненных",  header_format)
    worksheet_a.write(1, 4, "Ср время выполнения",  header_format)
    worksheet_a.write(1, 5, "Эффективность",  header_format)
    row = 1
    for key in my_dict:
       if len(my_dict[key].avg) == 0:
          my_dict[key].aver = 0.1
       else:
        mn = mean(my_dict[key].avg)
        if mn == 0: mn=0.1
        my_dict[key].aver = mn
       
        my_dict[key].eff = (my_dict[key].countsuc/mn)*100
    for smth in (sorted(my_dict.values(), key=operator.attrgetter('eff'), reverse=True)):
       row+=1
       name = "(" + str(smth.id.id) +") " +  smth.id.name + " " +  smth.id.surname
       
       worksheet_a.write(row, 0, name,  data_format)
       worksheet_a.write(row, 1, smth.count,  data_format)
       worksheet_a.write(row, 2, smth.countsuc,  data_format)
       if smth.count == 0: smth.count=0.1
       worksheet_a.write(row, 3, smth.countsuc/smth.count,  percent_format)
       worksheet_a.write(row, 4, smth.aver,  data_format)
       worksheet_a.write(row, 5, smth.eff,  eff_format)
        
    
    bar_chart.add_series(
     {
        "name": "График эффективности",
        "categories": "='Анализ успешности (SYS)'!$A$3:$A$"+str(row+1),
        "values": "='Анализ успешности (SYS)'!$F$3:$F$"+str(row+1),
     }
    )
    worksheet_a.insert_chart("H1", bar_chart)
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
def Displayonsite():
    my_dict = {}
    datareq = RepairRequests.objects.all()
    
    for data in datareq:
     
     if  data.req_status=="Выполнено":
        key = data.sys_id
        
        if my_dict.get(key)!=None:
            my_dict[key].countsuc+=1
            my_dict[key].count+=1
            c = str(data.req_cmp_date).replace(':00+00:00', '')
            C = datetime.strptime(c, format)
            b = str(data.req_acc_date).replace(':00+00:00', '')
            B = datetime.strptime(b, format)
            diff = C - B
            my_dict[key].avg.append(int(diff.total_seconds()/3600))
        
            
        else:
           my_dict[key] = ForExc(id=key)
           my_dict[key].countsuc+=1
           my_dict[key].count+=1
           c = str(data.req_cmp_date).replace(':00+00:00', '')
           C = datetime.strptime(c, format)
           b = str(data.req_acc_date).replace(':00+00:00', '')
           B = datetime.strptime(b, format)
           diff = C - B
           
           my_dict[key].avg.append(int(diff.total_seconds()/3600))
           
     elif data.req_status=="В процессе":
        key =data.sys_id
        if my_dict.get(key)!=None:
            my_dict[key].count+=1
        else:
           my_dict[key] = ForExc(id=key)
   
    for key in my_dict:
       if len(my_dict[key].avg) == 0:
          my_dict[key].aver = 0.1
       else:
        mn = mean(my_dict[key].avg)
        if mn == 0: mn=0.1
        my_dict[key].aver = mn
       
        my_dict[key].eff = (my_dict[key].countsuc/mn)*1000
    A = {}
    row = 0
    for smth in (sorted(my_dict.values(), key=operator.attrgetter('eff'), reverse=True)):
       row+=1
       b = {}
       name = "(" + str(smth.id.id) +") " +  smth.id.name + " " +  smth.id.surname
       b["name"] = name
       b["req_count"] = smth.count
       b["req_complete_count"] = smth.countsuc
       if smth.count == 0: smth.count=0.1
       b["percent_of_complete"]  = (smth.countsuc/smth.count)*100
       b["avg_time"] = smth.aver
       b["eff"] = int(smth.eff)
       if b["eff"]>100: b['eff'] = 99
       A[row]  = b
    
    return A
       


