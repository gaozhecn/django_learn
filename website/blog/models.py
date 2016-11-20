#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
#数据库相关的类
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    intime = models.DateTimeField()
    sex = models.IntegerField()
    class Meta:
        db_table = 'student'
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'teacher'
