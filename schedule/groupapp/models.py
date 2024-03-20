from django.db import models

class modelGroup(models.Model):
    chatId = models.CharField(max_length=100)
    groupId = models.CharField(max_length=100)
    degree = models.CharField(max_length=20, choices=[('bachelor', 'Bachelor'), ('magister', 'Magister'),])
    studyForm = models.CharField(max_length=20, choices=[('full-time', 'Full-time'), ('part-time', 'Part-time')])
    course = models.IntegerField(default=1)

    def __str__(self):
        return self.chatId