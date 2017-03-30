from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50,default= "")
    price = models.CharField(max_length=50,default= "")
    UserIdfk = models.CharField(max_length=50,default= "")
    gameURL = models.URLField(max_length=50,default= "")


class Transaction(models.Model):
    """TODO"""
    pass

class Score(models.Model):
    """TODO"""
    pass

class Profile(models.Model):
    """TODO"""
    pass

class Users(models.Model):
    name = models.CharField(max_length=50)
    userName = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
