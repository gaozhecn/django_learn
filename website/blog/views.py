#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
def index(request):
    return HttpResponse("<h1>Helle World!</h1>")

def index_template(request):
    t = loader.get_template("index.html")  # 加载模板
    c = Context({})  # 想模板提供数据
    return HttpResponse(t.render(c))