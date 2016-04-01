from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class AllClubs(models.Model):
    id = models.AutoField(primary_key = True)    
    name=models.CharField(max_length=96, unique=True, blank=True)
    
    
class AllManager(models.Model):
    id = models.AutoField(primary_key = True)
    name=models.CharField(max_length=96, unique=True, blank=True)
    nationality=models.CharField(max_length=96, unique=True, blank=True)
    

class AllPlayers(models.Model):
    id = models.AutoField(primary_key = True)    
    name=models.CharField(max_length=96, unique=True, blank=True)
    nationality=models.CharField(max_length=96, unique=True, blank=True)


class AllStadium(models.Model):
    id = models.AutoField(primary_key = True)
    capacity=models.IntegerField(unique=True, blank=True)
    location=models.CharField(max_length=96, unique=True, blank=True)
    
class AllTrophies(models.Model):
    id = models.AutoField(primary_key = True)
    name=models.CharField(max_length=96, unique=True, blank=True)
    notrophies=models.IntegerField(unique=True, blank=True)