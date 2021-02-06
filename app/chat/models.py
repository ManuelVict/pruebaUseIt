from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=220, blank=False, null=False)
    dateJoin = models.DateTimeField()
    lastSeen = models.DateTimeField()

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateMessage = models.DateTimeField()

