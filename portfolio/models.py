from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateTimeField()
	version = models.CharField(max_length=20)
	summary = models.CharField(max_length=200)

	def __str__(self):
		return title + " , " + version

class File(models.Model):
	size = models.CharField(max_length=20)
	file_type = models.CharField(max_length=20)
	path = models.CharField(max_length=100)
	number = models.IntegerField
	author = models.CharField(max_length=20)
	date = models.DateTimeField()
	project = models.ForeignKey(Project)