from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100) # 닉네임
    university = models.CharField(max_length=50)# 대학
    location = models.CharField(max_length=200) # 거주지