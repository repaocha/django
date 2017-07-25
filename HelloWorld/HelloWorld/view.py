#!/usr/bin/python
#  -*-coding:utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render #增加render代替HttpResponse,用于向模板提交数据

def hello(request):
	context    ={}
	context['hello']='Hello World!'
	return render(request,'hello.html',context)