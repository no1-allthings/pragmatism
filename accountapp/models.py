from django.db import models

# Create your models here.

class Hello(models.Model):
    text = models.CharField(max_length=255, name=False)
