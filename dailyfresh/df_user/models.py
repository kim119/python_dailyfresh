# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

"""用户信息表"""


class Userinfo(models.Model):
    uname = models.CharField(max_length=20)  # 名字
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    ushow = models.CharField(max_length=30)  # 收货地址
    uaddress = models.CharField(max_length=100)
    uyoubian = models.CharField(max_length=6)  # 邮编
    uphone = models.CharField(max_length=11)  # 电话
