#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
import datetime
'''django_base1视频'''
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
'''django_base4视频
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
    book_list = ["python","C++","C","java"]
    p = person("haha",22,"female")
    #c3 = Context({"p":p})#传入类的对象
    c4 = Context({"book_list":book_list} )
    return HttpResponse(t.render(c4))
'''
def index_template(request):
    t = loader.get_template("index.html")  # 加载模板
    book_list = ["python","C++","C","java"]
    book_list2 = []
    #for book in book_list:#很不优雅的转换方法，放在模板里面更优雅
    #    book_list2.append(book.upper())

    c4 = Context({"book_list":book_list,"title":"django","data":datetime.datetime.now()} )
    return HttpResponse(t.render(c4))

def time(request):
    t = loader.get_template("time.html")
    #第一种方式传值
    id = request.GET.get("id")#http://127.0.0.1:8000/blog/time/?id=123
    name = request.GET.get("name")#http://127.0.0.1:8000/blog/time/?id=jhvhjvjh&name=sdasd
    c = Context({"time":datetime.datetime.now(),"id":id,"name":name})
    return HttpResponse(t.render(c))

def foo(request,idp,namep):
    #第二种传值方式
    t = loader.get_template("time.html")
    c = Context({"time":datetime.datetime.now(),"id":idp,"name":namep})#http://127.0.0.1:8000/blog/foo/1234/as23424sd/
    return HttpResponse(t.render(c))

def bar(request,id,name):
    #第二种传值方式
    t = loader.get_template("time.html")
    c = Context({"time":datetime.datetime.now(),"id":id,"name":name})#http://127.0.0.1:8000/blog/foo/1234/as23424sd/
    return HttpResponse(t.render(c))