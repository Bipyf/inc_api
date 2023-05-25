from django.urls import path
from .apis import PositionViewSet, AnalysView, DownloadView, LoginView, EmpViewSet, WorkCatViewSet, ComputerViewSet, RequestsViewSet, TokenView, RegisterView, RoleView, HRViewSet, AdmViewSet, SysViewSet, EveryViewSet
from .apis import MyCompView, ProfileView, ProfilesView, TasksViewSet, TasksView, ForSys
from rest_framework import routers


urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('verify-token/', TokenView.as_view(), name='login'),
    path('view-role/', RoleView.as_view(), name='role'),
    path('register/', RegisterView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='login'),
    path('profiles/', ProfilesView.as_view(), name='login'),
    path('dwn/', DownloadView.as_view(), name='login'),
    path('an/', AnalysView.as_view(), name='login'),
    path('tasks/', TasksView.as_view(), name='login'),
    path('mycomp/', MyCompView.as_view(), name='login'),
    path('forsys/', ForSys.as_view(), name='login'),
]

router = routers.DefaultRouter()
router.register('api/position', PositionViewSet, 'positions')
router.register('api/employee', EmpViewSet, 'employees')
router.register('api/every', EveryViewSet, 'every')
router.register('api/hrs', HRViewSet, 'hrs')
router.register('api/sysadm', SysViewSet, 'sys')
router.register('api/adm', AdmViewSet, 'adms')
router.register('api/job_catalogue', WorkCatViewSet, 'work_catalogue')
router.register('api/computer', ComputerViewSet, 'computers')
router.register('api/request', RequestsViewSet, 'requests')
router.register('api/task', TasksViewSet, 'tasks')

urlpatterns+= router.urls
