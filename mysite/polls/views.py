# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from . models import Question

# Create your views here.

#def index(request):
#	lastest_question_list=Question.objects.order_by('-pub_date')[:5]
#	output=', '.join([p.question_text for p in lastest_question_list])   #显示系统中最新发布的5条questions记录,并用逗号分隔.
#	return HttpResponse(output)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')
#   context = RequestContext(request, {
#        'latest_question_list': latest_question_list,
#    })
#    return HttpResponse(template.render(context))
#载入polls/index.html模板,并传给它一个context.Context是一个字典,将模板变量的名字映射到Python 对象.

def index(request):
	lastest_question_list=Question.objects.order_by('-pub_date')[:5]
	context={'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	return HttpResponse("You're looking at question%s." % question_id)

def results(request,question_id):
	response="You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You're voting on question %s." % question_id)