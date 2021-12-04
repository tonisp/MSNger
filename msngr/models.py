from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')



class Room(models.Model):
    name = models.CharField(max_length=20, unique=True)
    users = models.ManyToManyField(Profile)



class Message(models.Model):
    value = models.CharField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Room,on_delete=models.DO_NOTHING)

