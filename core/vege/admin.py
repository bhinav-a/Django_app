from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Receipe)
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
