from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Position, Emp, Work_Catalogue, Computers, RepairRequests, CustomUser, Tasks
from django.contrib.auth.models import Group



class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Position
        fields = '__all__'
class EmpSerializer(serializers.ModelSerializer):
    workplace = serializers.CharField(source='workplace_id.workplace_name', read_only=True)
    class Meta:
        model= Emp
        fields = '__all__'
class SysSerializer(serializers.ModelSerializer):
    workplace = serializers.CharField(source='workplace_id.workplace_name', read_only=True)
    class Meta:
        model= Emp
        fields = '__all__'
class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model= Emp
        fields = '__all__'
class AdminSerializer(serializers.ModelSerializer):
    workplace = serializers.CharField(source='workplace_id.workplace_name', read_only=True)
    class Meta:
        model= Emp
        fields = '__all__'
class WorkCatSerializer(serializers.ModelSerializer):
    class Meta:
        model= Work_Catalogue
        fields = '__all__'
class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Computers
        fields = '__all__'
class RequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model= RepairRequests
        fields = '__all__'
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'surname','password', 'gender', 'role', 'phone', 'email')
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        tokendata = Token.objects.create(user=user)
        tokendata.save()
        if self.validated_data["role"] == "Сотрудник":
            gr = Group.objects.get(name="Employee")
            user.groups.add(gr)
        if self.validated_data["role"] == "HR":
            gr = Group.objects.get(name="HR")
            user.groups.add(gr)
        if self.validated_data["role"] == "Сисадмин":
            gr = Group.objects.get(name="SysAdmin")
            user.groups.add(gr)
        if self.validated_data["role"] == "Админ":
            gr = Group.objects.get(name="Admin")
            user.groups.add(gr)
        return user
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tasks
        fields = '__all__'