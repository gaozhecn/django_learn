#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import include, url, patterns
from django.contrib import admin

'''
#以前的默认方式
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index','blog.views.index'),
    url(r'^blog/template','blog.views.index_template'),
    url(r'^time','blog.views.time'),
]
'''

#视频给出的新的形式
#urlpatterns = patterns("blog.views",
#                        url(r'^admin/', include(admin.site.urls)),
#                        url(r'^blog/index','index'),
#                        url(r'^blog/template','index_template'),
#                       )
#分离的方式，方便管理，更加清晰。配置简洁
#urlpatterns += patterns("blog.views",
#                        url(r'^time','time'),
#                       )
#每个站点管理自己的URL,更加简洁，优雅
urlpatterns = patterns("blog.views",
                       url(r'blog/',include('blog.urls')),
                       )
