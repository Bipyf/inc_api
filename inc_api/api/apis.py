from .models import Position, Emp, Work_Catalogue, Computers, RepairRequests, Tasks
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, views, status ,generics
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json
from . import export_report


from .serializers import  TaskSerializer, PositionSerializer, EmpSerializer, WorkCatSerializer, ComputerSerializer,  RequestsSerializer, CustomUserSerializer, SysSerializer, AdminSerializer, HRSerializer


class TokenView(views.APIView):
    def get(self, request):
        return Response(data={"loggedIn":True})
class RoleView(views.APIView):
    def get(self, request):
        return Response(data={"role":self.request.user.groups.all()[0].name})
    
class RegisterView(generics.CreateAPIView):
    permission_classes=[]
    serializer_class = CustomUserSerializer
        
        

class LoginView(views.APIView):
    permission_classes = []
    def post(self, request):
        username = self.request.data.get("username")
        password =self.request.data.get("password")

        user = authenticate(username=username, password = password)

        if user is not None:
            response = {
                "msg":"Success",
                "token":user.auth_token.key,
                "role":user.groups.all()[0].name,
                "id":str(user.id)
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"msg":"Invalid username or password"})
        
class ProfileView(views.APIView):
    def get(self, request):
        print(request.user.id, " ", Emp.objects.filter(id = self.request.user.id))
        content = serializers.serialize('json' ,Emp.objects.filter(id = self.request.user.id))
        if content!=None:
            result = json.dumps(content)
            result = eval(result)
            response =  HttpResponse(result, content_type='application/json')
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        else: 
            return HttpResponse("404")
    def put(self, request):
         obj = Emp.objects.filter(id = self.request.user.id)
         obj.update(**self.request.data)
         content = serializers.serialize('json' ,obj)
         result = json.dumps(content)
         result = eval(result)
         response =  HttpResponse(result, content_type='application/json')
         return response
class ProfilesView(views.APIView):
    def get(self, request):
        print(request.user.id, " ", Emp.objects.filter(id = self.request.user.id))
        obj = Emp.objects.filter(id = self.request.user.id)
        content = HRSerializer(obj, many = True).data
        if content!=None:
            result = json.dumps(content,ensure_ascii=False)
            response =  HttpResponse(result, content_type='application/json')
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        else: 
            return HttpResponse("404")


class MyCompView(views.APIView):
    def get(self, request):
        print(request.user.id, " ", Computers.objects.filter(owner = self.request.user.id))
        obj = Computers.objects.filter(owner = self.request.user.id)
        content = ComputerSerializer(obj, many = True).data
        if content!=None:
            result = json.dumps(content,ensure_ascii=False)
            response =  HttpResponse(result, content_type='application/json')
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        else: 
            return HttpResponse("404")
    def post(self, request):
        req_desc = self.request.data['req_desc']
        emp_id = Emp.objects.filter(id = self.request.user.id)[0]
        computer = Computers.objects.filter(id = self.request.data['computer'])[0]
        req_status = "Принято"
        obj = RepairRequests(req_desc = req_desc, emp_id = emp_id, computer = computer, req_status = req_status)
        obj.save()
        return HttpResponse('200')
class ForSys(views.APIView):
    def put(self, request):
         obj = RepairRequests.objects.filter(id = self.request.data['id'])[0]
         obj.req_status = self.request.data['req_status']
         obj.sys_id = Emp.objects.filter(id = self.request.user.id)[0]
         obj.save()
         content = serializers.serialize('json' ,obj)
         result = json.dumps(content)
         result = eval(result)
         response =  HttpResponse(result, content_type='application/json')
         return response
    def delete(self, request):
        obj = RepairRequests.objects.filter(id = self.request.data['id'])[0]
        obj.delete()
        return HttpResponse('200')
        
        
class DownloadView(views.APIView):
    def get(self, *args, **kwargs):  
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
        xlsx_data = export_report.WriteToExcel()
        response.write(xlsx_data)
        return response
class AnalysView(views.APIView):
    def get(self, *args, **kwargs):
        
        xlsx_data = export_report.Displayonsite()
        response = HttpResponse(content_type = 'application/json')
        xlsx_data = json.dumps(xlsx_data, ensure_ascii=False)
        response.write(xlsx_data)
        return response
class TasksView(views.APIView):
    def get(self, *args, **kwargs):
        content = serializers.serialize('json' ,Tasks.objects.filter(id = self.request.user.id))
        if content!=None:
            result = json.dumps(content)
            result = eval(result)
            response =  HttpResponse(result, content_type='application/json')
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "GET"
            response["Access-Control-Allow-Headers"] = "*"
            return response
        else: 
            return HttpResponse("404")
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
        ]
    
    serializer_class = PositionSerializer
    
class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.filter(position='Сотрудник')
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = EmpSerializer
class SysViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.filter(position='Сисадмин')
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = SysSerializer
class AdmViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.filter(position='Админ')
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = AdminSerializer
class HRViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.filter(position='HR')
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = EmpSerializer
class EveryViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = HRSerializer
class WorkCatViewSet(viewsets.ModelViewSet):
    queryset = Work_Catalogue.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = WorkCatSerializer
    
class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computers.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = ComputerSerializer

class RequestsViewSet(viewsets.ModelViewSet):
    queryset = RepairRequests.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = RequestsSerializer
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
        ]
    serializer_class = TaskSerializer