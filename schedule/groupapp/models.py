from django.db import models

class modelGroup(models.Model):
    chatId = models.CharField(max_length=100)
    groupId = models.CharField(max_length=100)