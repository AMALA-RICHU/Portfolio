from django.db import models

# Create your models here.

class Job(models.Model):
	# images 
	image = models.ImageField(upload_to='images/') #upload images to this folder which gets created once we add
	#summary
	summary = models.CharField(max_length = 200) #how much space is it going to take up




	def __str__(self): # description of objects in the admin panel
		return self.summary