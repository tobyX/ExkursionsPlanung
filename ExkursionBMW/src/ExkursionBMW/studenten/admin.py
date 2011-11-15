from studenten.models import Student
from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    list_display = ('nachname', 'vorname', 'email')

admin.site.register(Student, StudentAdmin)