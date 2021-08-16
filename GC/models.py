from django.db import models

class UserD(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthdate = models.CharField(max_length=20)
    aadharno = models.CharField(max_length=12)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=32)
    status = models.CharField(max_length=20,default=None)
    role = models.CharField(max_length=20,default=None)

class Admin(models.Model):
    aid = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=32)