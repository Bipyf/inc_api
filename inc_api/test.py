from datetime import datetime
class ForExc():
   id = 0
   count = 0
   countsuc = 0
   avg = []
   def __init__(self,id):
       self.id = id

format = '%Y-%m-%d %H:%M'



j = '2023-05-08T13:26Z'
f = '2023-05-09T4:12Z'
f = f.replace('T', ' ')
f = f.replace('Z', '')

j = j.replace('T', ' ')
j = j.replace('Z', '')

F = datetime.strptime(f, format)
J = datetime.strptime(j, format)

diff = F - J
res = diff.total_seconds()/3600


print(int(res))


# my_dict = {}
# datareq = [1,2,1,2,1,3]

# for data in datareq:
#      print('work')
#      if  data==1:
#         if my_dict.get(str(data))!=None:
#             my_dict[str(data)].countsuc+=1
#         else:
#             my_dict[str(data)] = ForExc(id=data)
#             my_dict[str(data)].countsuc+=1
#      elif data ==2:
#          if my_dict.get('1')!=None:
#              my_dict['1'].count+=1
#          else:
#             my_dict[str(data)] = ForExc(id=1)
#      elif data ==3:
#          if my_dict.get(str(data))!=None:
#              my_dict[str(data)].countsuc+=1
#          else:
#             my_dict[str(data)] = ForExc(id=data)
#             my_dict[str(data)].countsuc+=1

# print(my_dict)
# print(my_dict['3'].countsuc)