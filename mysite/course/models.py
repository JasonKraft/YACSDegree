'''
Contributor(s): Jason Kraft
Description: Contains model declarations for Department,
	Course, and CourseDates.
'''
# === Imports ===
from django.db import models


# === Model declarations ===
# Every Course has a Department
# Every coursedate corresponds to a course and has a unique CRN

class Department(models.Model):
	name = models.CharField(max_length=200, unique=True)
	shorthand = models.CharField(max_length=5, unique=True)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	department = models.ForeignKey('Department')
	number = models.PositiveSmallIntegerField()
	credits = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return self.name

class CourseDate(models.Model):
	course = models.ForeignKey('Course')
	CRN = models.PositiveIntegerField(unique=True)
	slug = models.SlugField(unique=True)
	section = models.PositiveSmallIntegerField(unique=True)

	def __unicode__(self):
		return self.CRN