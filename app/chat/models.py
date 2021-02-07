from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=220, blank=False, null=False)
    dateJoin = models.DateTimeField()
    lastSeen = models.DateTimeField()

    def _str_(self):
        return self.nick.username

def createUser(sender, instance, created, **kwargs):
    if created:
        user.objects.create(nick=instance)

def saveUser(sender, instance, **kwargs):
    instance.user.save()

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateMessage = models.DateTimeField()

