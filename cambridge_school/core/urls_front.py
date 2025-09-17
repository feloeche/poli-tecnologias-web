from django.urls import path
from . import views_front as v


app_name = 'front'


urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),

    path('areas/', v.AreaListView.as_view(), name='areas_list'),
    path('areas/new/', v.AreaCreateView.as_view(), name='areas_new'),
    path('areas/<int:pk>/edit/', v.AreaUpdateView.as_view(), name='areas_edit'),
    path('areas/<int:pk>/delete/', v.AreaDeleteView.as_view(), name='areas_delete'),

    path('offices/', v.OfficeListView.as_view(), name='offices_list'),
    path('offices/new/', v.OfficeCreateView.as_view(), name='offices_new'),
    path('offices/<int:pk>/edit/', v.OfficeUpdateView.as_view(), name='offices_edit'),
    path('offices/<int:pk>/delete/', v.OfficeDeleteView.as_view(), name='offices_delete'),

    path('classrooms/', v.ClassroomListView.as_view(), name='classrooms_list'),
    path('classrooms/new/', v.ClassroomCreateView.as_view(), name='classrooms_new'),
    path('classrooms/<int:pk>/edit/', v.ClassroomUpdateView.as_view(), name='classrooms_edit'),
    path('classrooms/<int:pk>/delete/', v.ClassroomDeleteView.as_view(), name='classrooms_delete'),

    path('employees/', v.EmployeeListView.as_view(), name='employees_list'),
    path('employees/new/', v.EmployeeCreateView.as_view(), name='employees_new'),
    path('employees/<int:pk>/edit/', v.EmployeeUpdateView.as_view(), name='employees_edit'),
    path('employees/<int:pk>/delete/', v.EmployeeDeleteView.as_view(), name='employees_delete'),

    # Reports
    path('reports/employees/', v.EmployeeReportView.as_view(), name='employee_report'),
]

