# YACSDegree
YACS Degree Maker

##Preliminary Outline:

This list is incomplete and not organized.

 * We need to agree on a unified (or unifiable) database structure
 * Create a method for storing user credentials/information
 * Ability to work on a degree without publishing
 * Degree search tool
 * A means of creating a degree
 * A means of delete a degree
 * A means of modifying a degree

 ##Preliminary Process of Creating a Course
 1. Enter the name of the class
 2. Select a department and a course number (possibly, select a level [1000, 2000, 4000, etc.] and have course number autogenerate)
 3. Select if the class is limited to certain majors (might run into an issue if the major does not exists but the class is needed to create the major)
 4. Select any preexisting courses that are prerequisites for this course.
 5. Select if this course is only available for a certain semester.
 6. Enter a brief description of a class
 7. [possible] Enter a professor teaching the class

 ##Preliminary Process of Creating a Degree

 1. Enter a name and short-hand
 2. Select a department
 3. Select a semester (defaults to current semester)
 4. Enter degree rules GUI
 5. Create a new rule. This rule can be:
 	- required course + alternative
 	- science electives*
 	- HASS electives*
 	- free electives*
	- depth/breadth requirement (what does this even mean?)
 6. Rinse. Repeat. Profit (for each new rule).
 7. Display number of required credits.
 8. Save and/or publish degree

*Electives can differ for each degree.


 ##Database Oraganization
 *Database needs to be integrated/compatible with the code we produce in Django, as data needs to easily accessible.

 *PROPOSAL FOR UNIFIED STRUCTURE
	1.  Tables for each degree, where each degree has multiple tables containing rules for said degree.
	2.  Master table containing all courses and their respective shorthands.
	3.  Multiple versions of degrees may be necessary to be stored in database to handle different enrollment years.
	4.  Rule system needs to be created for each individual course in the master table.