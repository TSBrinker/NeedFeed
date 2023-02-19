from django.db import models

# Create your models here.
class Primary_Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)