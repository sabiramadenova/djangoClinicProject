from django.urls import path, include
from rest_framework import routers
from clinicapi.views import *


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'specialties', SpecialityViewSet)
router.register(r'schedules', ScheduleViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

