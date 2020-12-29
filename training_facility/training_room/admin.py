from django.contrib import admin
from .models import Lecturer, Degree, Student, Courses

admin.site.register(Lecturer)
admin.site.register(Degree)
admin.site.register(Student)
admin.site.register(Courses)


