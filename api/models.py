from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Chat(models.Model):
    sender = models.CharField(max_length=200, null=True, blank=True)
    reciver = models.CharField(max_length=200, null=True, blank=True)
    whosend = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=20000, null=True, blank=True)
    voicerecord = models.FileField(
        upload_to='audios', blank=True, null=True, default='11'
    )
    created = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.sender)


class UserProfile(models.Model):
    user = models.CharField(max_length=200, blank=True,
                            null=True, db_index=True, unique=True, default='')
    avatar = models.FileField(
        upload_to='images', blank=True, null=True
    )

    def __str__(self):
        return self.user
