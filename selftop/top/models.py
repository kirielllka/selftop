from django.db import models
from django.contrib.auth.models import User
class HomeworkModel(models.Model):
    name =models.CharField(max_length=100)
    describtion =models.CharField(blank=True, max_length=1000)
    date = models.DateTimeField(blank=True)
    file = models.FileField(blank=True)
    home = models.FileField(blank=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)

class Homework(models.Model):
    file = models.FileField(upload_to='media/')
