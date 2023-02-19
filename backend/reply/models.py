from django.db import models
from post.models import Post
from authentication.models import User
import datetime

# Create your models here.

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    timestamp = models.DateField(default=datetime.date.today)