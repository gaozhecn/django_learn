#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
def index(request):
    return HttpResponse("<h1>Helle World!</h1>")
''' django_base2视频
def index_template(request):
    t = loader.get_template("index.html")  # 加载模板
    c = Context({})  # 想模板提供数据
    return HttpResponse(t.render(c))
'''

'''django_base3视频
class person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say(self):
        return "ma name is " + self.name

def index_template(request):
    t = loader.get_template("index.html")  # 加载模板
    #c1 = Context({"title":"django","name":"xiaogao"})  # 通过模板变量加载模板数据
    user = {"name": "tom", "age": 23, "sex": "male"}  # 通过字典向页面提供数据
    #c2 = Context({"title":"django","user":user}
    book_list = ["python","c++","C","java"]
    p = person("haha",22,"female")
    #c3 = Context({"p":p})#传入类的对象
    c4 = Context({"book_list":book_list} )
    return HttpResponse(t.render(c4))
'''
class person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def say(self):
        return "ma name is " + self.name

def index_template(request):
    t = loader.get_template("index.html")  # 加载模板
    #c1 = Context({"title":"django","name":"xiaogao"})  # 通过模板变量加载模板数据
    user = {"name": "tom", "age": 0, "sex": "male"}  # 通过字典向页面提供数据
    c2 = Context({"title":"django","user":user})
    book_list = ["python","","C","java"]
    p = person("haha",22,"female")
    #c3 = Context({"p":p})#传入类的对象
    c4 = Context({"book_list":book_list} )
    return HttpResponse(t.render(c4))
