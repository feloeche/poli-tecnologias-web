from django import forms
from .models import Area, Office, Classroom, Employee


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name']


class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['code', 'area']


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['code']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['document_id', 'full_name', 'role', 'professor_type', 'area', 'office']

