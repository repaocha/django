# -*- coding:utf-8 -*-
from django.shortcuts import  get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from . models import Question
from django.http import Http404

# Create your views here.

#def index(request):
#	lastest_question_list=Question.objects.order_by('-pub_date')[:5]
#	output=', '.join([p.question_text for p in lastest_question_list])   #显示系统中最新发布的5条questions记录,并用逗号分隔.
#	return HttpResponse(output)

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#   template = loader.get_template('polls/index.html')           #模板的名字:polls/index.html
#   context = RequestContext(request, {
#        'latest_question_list': latest_question_list,
#    })
#    return HttpResponse(template.render(context))
#载入polls/index.html模板,并传给它一个context.Context是一个字典,将模板变量的名字映射到Python 对象.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

#def detail(request,question_id):
#	return HttpResponse("You're looking at question%s." % question_id)

#def detail(request,question_id):                       #引发一个404错误
#	try:
#		question=Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exist"
#	return render(request,'polls/detail.html',{'question':question})

def detail(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})
#get_object_or_404() 函数将模型Question作为它的第一个参数，任意数量的关键字参数作为它的第二个参数，
#它会将这些关键字参数传递给模型管理器中的get() 函数,如果对象不存在，引发一个 Http404异常.

def results(request,question_id):
	response="You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You're voting on question %s." % question_id)