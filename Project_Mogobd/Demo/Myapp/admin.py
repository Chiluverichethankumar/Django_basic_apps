from django.contrib import admin
from .models import TodoItem, Student
# Register your models here.

admin.site.register(TodoItem)
admin.site.register(Student)