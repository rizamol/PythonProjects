from django.db import models
import datetime

# Create your models here.



class Task(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    msg = models.TextField(max_length=150)
    date = models.DateField(default=datetime.date.today)
    img = models.ImageField(upload_to="images")

