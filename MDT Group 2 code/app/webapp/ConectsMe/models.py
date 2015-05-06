from django.db import models

# Create your models here.

class SupportedDevices(models.Model):
	device_text = models.CharField(max_length=200)

class TempUsers(models.Model):
	username = models.CharField(max_length=50)
	passw = models.CharField(max_length=50)
