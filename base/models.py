from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime
# Create your models here.

class User(AbstractUser):
  friends=models.ManyToManyField('User', blank=True)
  bio = models.TextField(max_length=400, blank=True)







class FriendRequest(models.Model):
  from_user = models.ForeignKey(User, related_name="from_user",on_delete=models.CASCADE)
  to_user = models.ForeignKey(User, related_name="to_user",on_delete=models.CASCADE)



