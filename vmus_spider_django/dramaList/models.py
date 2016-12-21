from django.db import models

# Create your models here.

class Show(models.Model):
    show_name = models.CharField(max_length=50)
