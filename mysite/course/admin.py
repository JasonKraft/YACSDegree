'''
Contributor(s): Jason Kraft
Description: Describes how the course application
	is displayed in the admin control panel.
'''
# === Imports ===
from django.contrib import admin
from course.models import *

# === ModelAdmin declarations ===
class DepartmentAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('shorthand',)}
	list_display = ('shorthand', 'name')
	search_fields = ['name', 'shorthand']

class CourseAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}
	list_display = ('name', 'department', 'number', 'credits')
	search_fields = ['name']


class CourseDateAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('CRN',)}
	list_display = ('CRN', 'course', 'section')
	search_fields = ['CRN']

# === Registrations ===
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDate, CourseDateAdmin)