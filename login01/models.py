from django.db import models


# Create your models here.

class RegisterUser(models.Model):
    User_id = models.CharField(max_length=120, blank=False, primary_key=True)
    User_passwd = models.CharField(max_length=120, blank=False)
