# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),     #ex:/polls/
    url(r'^(?p<question_id>[0-9]+)/$',views.detail,name='detail'),   #ex:/polls/5/
    url(r'^(?p<question_id>[0-9]+)/results/$',views.results,name='result'),  #ex:/polls/5/results/
    url(r'^(?p<question_id>[0-9]+)/vote/$',views.vote,name='vote'),   #ex:/polls/5/vote/    
]