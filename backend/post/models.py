from django.db import models
from authentication.models import User
import datetime

# Create your models here.
class Post(models.Model):
    timestamp = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)