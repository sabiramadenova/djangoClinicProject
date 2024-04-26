from rest_framework import serializers
from website.models import Post, Doctor, Patient, Schedule, Speciality, Department


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'date_published')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')
        read_only_fields = ('__all__', )


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    # department = DepartmentSerializer(read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Speciality
        fields = ('id', 'name', 'department')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    speciality = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all())

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'phone_number', 'email', 'speciality')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'phone_number', 'email')


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Schedule
        fields = ('id', 'doctor', 'patient', 'time_in', 'time_out', 'cabinet')


