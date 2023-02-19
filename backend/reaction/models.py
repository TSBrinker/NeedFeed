from django.db import models
from authentication.models import User
from post.models import Post

# Create your models here.
class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)