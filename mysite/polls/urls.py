# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

#urlpatterns=[
#   url(r'^$',views.index,name='index'),     #ex:/polls/
#    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),   #ex:/polls/5/
#    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='result'),  #ex:/polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),   #ex:/polls/5/vote/    
#]

#?P<question_id> 定义一个名字,它将用于标识匹配的模式;[0-9]+是匹配一串数字的正则表达式.

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]