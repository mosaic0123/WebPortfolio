from django.db import models

# Create your models here.
class Comment(models.Model):
	content = models.CharField(max_length=500)
	date = models.DateTimeField()
	parent = models.ForeignKey('self', null=True)
	image = models.CharField(max_length=200, null=True)
	username = models.CharField(max_length=50, null=True)


	def __str__(self):
		return self.content
