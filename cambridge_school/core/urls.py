from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AreaViewSet, OfficeViewSet, ClassroomViewSet, EmployeeViewSet, ReportsViewSet


router = DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'offices', OfficeViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'reports', ReportsViewSet, basename='reports')


urlpatterns = [
    path('', include(router.urls)),
]

