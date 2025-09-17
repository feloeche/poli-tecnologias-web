from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

from .models import Area, Office, Classroom, Employee
from .serializers import (
    AreaSerializer,
    OfficeSerializer,
    ClassroomSerializer,
    EmployeeSerializer,
)


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().order_by('name')
    serializer_class = AreaSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.select_related('area').all().order_by('code')
    serializer_class = OfficeSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all().order_by('code')
    serializer_class = ClassroomSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = (
        Employee.objects.select_related('area', 'office')
        .all()
        .order_by('full_name')
    )
    serializer_class = EmployeeSerializer


class ReportsViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def areas_employees(self, request):
        # Aggregated counts per area plus employees list
        areas = Area.objects.all().order_by('name')
        data = []
        for area in areas:
            employees = Employee.objects.filter(area=area).select_related('office').order_by('full_name')
            data.append({
                'area_id': area.id,
                'area_name': area.name,
                'employee_count': employees.count(),
                'employees': [
                    {
                        'id': e.id,
                        'document_id': e.document_id,
                        'full_name': e.full_name,
                        'role': e.role,
                        'professor_type': e.professor_type,
                        'office_code': e.office.code,
                    }
                    for e in employees
                ],
            })
        return Response(data)

# Create your views here.
