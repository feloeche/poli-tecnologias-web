from django.contrib import admin
from .models import Area, Office, Classroom, Employee


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'area')
    search_fields = ('code',)
    list_filter = ('area',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')
    search_fields = ('code',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'document_id', 'role', 'professor_type', 'area', 'office')
    search_fields = ('full_name', 'document_id')
    list_filter = ('role', 'professor_type', 'area')

# Register your models here.
