from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class client_signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=20)


class publisher_signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=20)


class banners_upload(models.Model):
    banner = models.ImageField(upload_to= "banners_image")
    pub_name = models.CharField(max_length=20)
    banner_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.BigIntegerField()


class feedback(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    msg=models.TextField()