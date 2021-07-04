from django.db import models


# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length=12, primary_key=True)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    role = models.CharField(max_length=8)

    def __str__(self):
        return self.userid
