from django.db import models

# Create your models here.
class Guest(models.Model):
	nama = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	answer = models.CharField(max_length=10)
	
	def __str__(self):
		return self.answer + '   ' + self.nama + ':        ' + self.email