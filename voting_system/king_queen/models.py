from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FirstYear(models.Model):
    GENDER = (
        ('King','King'),
        ('Queen','Queen')
    )
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='kingqueenIMG')
    gender = models.CharField(max_length=5,choices=GENDER,default='King')
    current_class = models.CharField(max_length=10,help_text="(eg. 1CST-12,A ...)")
    votes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class TheWhole(models.Model):
    GENDER = (
        ('King','King'),
        ('Queen','Queen')
    )
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='kingqueenIMG')
    gender = models.CharField(max_length=5,choices=GENDER,default='King')
    current_class = models.CharField(max_length=10,help_text="(eg. 1CST-12,A ...)")
    votes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name