import datetime

from django.db import models

from clinicProject import settings


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    description = models.TextField()
    text = models.TextField(blank=True, null=True)
    date_published = models.DateField(auto_now_add=True)


class Department(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=70)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.department.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patronymic}"


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_in = models.DateTimeField(default=datetime.datetime.now())
    time_out = models.DateTimeField(default=datetime.datetime.now())
    cabinet = models.CharField(max_length=10, default="Undefined")
