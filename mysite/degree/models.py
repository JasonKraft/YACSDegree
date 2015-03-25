

"Contributor(s): Zachary Ravichandran"
"Description: Contains model declarations for Degree "


# === Imports ===
from django.db import models


# === Model declarations ===
# Every Degree has a name and shorthand
# Every Degree has a semester and year created

class Semester(models.Model):
	SEMESTERS = (
		('SP', 'SPRING')
		('SM', 'SUMMER')
		('FL', 'FALL')
	)

	season = models.CharField(max_length=2, choices = SEMESTERS)
	

class Degree_Application(models.Model):
	SEMESTERS = (
		('SP', 'SPRING')
		('SM', 'SUMMER')
		('FL', 'FALL')
	)

	name = models.CharField(max_length=20, unique=True)
	shorthand = models.CharField(max_length=5, unique=True)
	semester = models.CharField(max_length=2, choices = SEMESTERS)
	year = models.CharField(max_length = 4)
	slug = models.SlugField(unique=True)



	def __unicode__(self):
		return self.name
