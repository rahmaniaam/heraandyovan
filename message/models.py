from django.db import models

# Create your models here.
class Surat(models.Model):
	dari = models.CharField(max_length=30)
	untuk = models.CharField(max_length=30)
	pesan = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	