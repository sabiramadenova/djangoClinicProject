from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
from clinicapi.serializers import PostSerializer, DoctorSerializer, PatientSerializer, DepartmentSerializer, SpecialitySerializer, ScheduleSerializer
from website.models import Post, Doctor, Patient, Schedule, Department, Speciality


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('-id')
    serializer_class = DepartmentSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all().order_by('-id')
    serializer_class = SpecialitySerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('first_name')
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('first_name')
    serializer_class = PatientSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all().order_by('-id')
    serializer_class = ScheduleSerializer

