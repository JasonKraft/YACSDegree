from django.contrib import admin
from degree.models import Semester, Degree, DegreeRequirement

# Register your models here.
class SemesterAdmin(admin.ModelAdmin):
	prepoulated_fields 	= {'slug' : ('season',)}
	list_display		= ('season', 'year')

class DegreeAdmin(admin.ModelAdmin):
	prepoulated_fields 	= {'slug' : ('name')}
	list_display		= ('name', 'shorthand')
	search_fields		= ['name']

class RequirementAdmin(admin.ModelAdmin):
	list_display 		= ('course', 'degree', 'semester')


admin.site.register(Semester, SemesterAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(DegreeRequirement, RequirementAdmin)