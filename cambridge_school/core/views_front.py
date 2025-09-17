from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.db.models import Count, Q

from .models import Area, Office, Classroom, Employee
from .forms import AreaForm, OfficeForm, ClassroomForm, EmployeeForm


class HomeView(TemplateView):
    template_name = 'home.html'


# Areas
class AreaListView(ListView):
    model = Area
    template_name = 'areas/list.html'
    context_object_name = 'items'
    paginate_by = 20


class AreaCreateView(CreateView):
    model = Area
    form_class = AreaForm
    template_name = 'areas/form.html'
    success_url = reverse_lazy('front:areas_list')


class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreaForm
    template_name = 'areas/form.html'
    success_url = reverse_lazy('front:areas_list')


class AreaDeleteView(DeleteView):
    model = Area
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('front:areas_list')


# Offices
class OfficeListView(ListView):
    model = Office
    template_name = 'offices/list.html'
    context_object_name = 'items'
    paginate_by = 20


class OfficeCreateView(CreateView):
    model = Office
    form_class = OfficeForm
    template_name = 'offices/form.html'
    success_url = reverse_lazy('front:offices_list')


class OfficeUpdateView(UpdateView):
    model = Office
    form_class = OfficeForm
    template_name = 'offices/form.html'
    success_url = reverse_lazy('front:offices_list')


class OfficeDeleteView(DeleteView):
    model = Office
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('front:offices_list')


# Classrooms
class ClassroomListView(ListView):
    model = Classroom
    template_name = 'classrooms/list.html'
    context_object_name = 'items'
    paginate_by = 20


class ClassroomCreateView(CreateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classrooms/form.html'
    success_url = reverse_lazy('front:classrooms_list')


class ClassroomUpdateView(UpdateView):
    model = Classroom
    form_class = ClassroomForm
    template_name = 'classrooms/form.html'
    success_url = reverse_lazy('front:classrooms_list')


class ClassroomDeleteView(DeleteView):
    model = Classroom
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('front:classrooms_list')


# Employees
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/list.html'
    context_object_name = 'items'
    paginate_by = 20


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/form.html'
    success_url = reverse_lazy('front:employees_list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/form.html'
    success_url = reverse_lazy('front:employees_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('front:employees_list')


# Reports
class EmployeeReportView(ListView):
    model = Employee
    template_name = 'reports/employee_report.html'
    context_object_name = 'employees'
    paginate_by = 50
    
    def get_queryset(self):
        return Employee.objects.select_related('area', 'office').all().order_by('area__name', 'office__code', 'full_name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Estadísticas generales
        context['total_employees'] = Employee.objects.count()
        context['total_professors'] = Employee.objects.filter(role=Employee.Role.PROFESSOR).count()
        context['total_administrative'] = Employee.objects.filter(role=Employee.Role.ADMINISTRATIVE).count()
        
        # Estadísticas por área
        context['area_stats'] = (
            Employee.objects
            .values('area__name')
            .annotate(
                total=Count('id'),
                professors=Count('id', filter=Q(role=Employee.Role.PROFESSOR)),
                administrative=Count('id', filter=Q(role=Employee.Role.ADMINISTRATIVE))
            )
            .order_by('area__name')
        )
        
        # Estadísticas por oficina
        context['office_stats'] = (
            Employee.objects
            .select_related('office', 'area')
            .values('office__code', 'office__area__name')
            .annotate(
                total=Count('id'),
                professors=Count('id', filter=Q(role=Employee.Role.PROFESSOR)),
                administrative=Count('id', filter=Q(role=Employee.Role.ADMINISTRATIVE))
            )
            .order_by('office__area__name', 'office__code')
        )
        
        return context


