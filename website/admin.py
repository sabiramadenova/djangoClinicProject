from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Speciality)
admin.site.register(Schedule)