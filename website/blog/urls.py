#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url, patterns
#blog这个APP管理自己的url。
urlpatterns = patterns("blog.views",
                        url(r'^index','index'),
                        url(r'^template','index_template'),
                       )
#第一种传值方式。http://127.0.0.1:8000/blog/time/?id=jhvhjvjh&name=sdasd
#在URL中得手动指定id=123,name=asd
urlpatterns += patterns("blog.views",
                        url(r'^time/','time'),
                        )
#第二种传值方式。#http://127.0.0.1:8000/blog/foo/1234/as23424sd/
#(\d{4})四个数字。(\w+)至少一个字符，可以包含数字。
urlpatterns += patterns("blog.views",
                        url(r'^foo/(\d{4})/(\w+)/$', 'foo'),
                        )
#第三种传值方式。http://127.0.0.1:8000/blog/bar/1234/as23424sd/
#视图函数的参数变量名字必须和模板变量名id、name相同,否则会报错
#好处，清晰的知道变量名字的意思。
urlpatterns += patterns("blog.views",
                        url(r'^bar/(?P<id>\d{4})/(?P<name>\w+)/$', 'bar'),
                        )