from django.db import models

# Create your models here.
class Session(models.Model):
    session_id= models.CharField(max_length = 64)
    session_status = models.CharField(max_length = 32)