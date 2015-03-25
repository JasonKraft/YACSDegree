'''Contributor(s):	Zachary Ravichandran
					Stephen Wood
Description: Contains model declarations for Degree '''


# === Imports ===
from django.db import models
#from course import Course 		#import the course table so that we can have DegreeRequirement have a key to it


# === Model declarations ===
# Every Degree has a name and shorthand
# Every Degree has a semester and year created
# Every DegreeRequirement has a course or list of courses, a degree that it is for, and a semester when it starts to be in effect

SEMESTERS = (					
		('SP', 'SPRING'),
		('SM', 'SUMMER'),
		('FL', 'FALL'),
	)
class Semester(models.Model):
	season		= models.CharField(max_length=2, choices = SEMESTERS)
	year 		= models.IntegerField()	#Could possibly be a dateField, but that requires selecting a certain day, which is unnecessary information
											#Also can make custom model field if needbe, int should be fine though as long as user does not dick around
	slug 		= models.SlugField(unique=True)

	def __unicode__(self):
		return u'%s %d' % (self.season, self.year)


class Degree(models.Model):
	name 		= models.CharField(max_length=20, unique=True)
	shorthand 	= models.CharField(max_length=5, unique=True)
	slug 		= models.SlugField(unique=True)

	def __unicode__(self):
		return self.name

class DegreeRequirement(models.Model):			#This is for a degree requirement with no options
	#course		= models.ForeignKey('Course')
	course 		= models.CharField(max_length=50)
	degree 		= models.ForeignKey('Degree')
	semester 	= models.ForeignKey('Semester')

	def __unicode__(self):
		return u'%s for %s in %s' %(self.course, self.degree.name, self.semester)