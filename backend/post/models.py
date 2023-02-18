from django.db import models
from authentication.models import User
from primary_category.models import Primary_Category
from secondary_category.models import Secondary_Category
import datetime


# Create your models here.
class Post(models.Model):
    timestamp = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    body = models.CharField(max_lengh=1000)
    primary_category = models.ForeignKey(Primary_Category, on_delete=models.PROTECT)
    secondary_category = models.ForeignKey(Secondary_Category, on_delete=models.PROTECT)
    #primary_category will indicate whether it is a need or a thankful report, secondary_category will indicate whether it is related to health, job, meals, family care, etc.