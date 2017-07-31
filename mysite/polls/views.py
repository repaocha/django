# -*- coding:utf-8 -*-
#from django.shortcuts import  get_object_or_404, render
#from django.http import HttpResponse
#from django.template import RequestContext, loader
#from django.views import generic
#from django.http import Http404
#from django.http import HttpResponseRedirect,HttpResponse
#from django.core.urlresolvers import reverse

#from .models import Choice, Question

#from . models import Choice,Question

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

#def index(request):
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	context = {'latest_question_list': latest_question_list}
#	return render(request, 'polls/index.html', context)

#视图
#def detail(request,question_id):
#	return HttpResponse("You're looking at question%s." % question_id)

#def detail(request,question_id):                       #引发一个404错误
#	try:
#		question=Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404("Question does not exist"
#	return render(request,'polls/detail.html',{'question':question})

#def detail(request,question_id):
#	question=get_object_or_404(Question,pk=question_id)
#	return render(request,'polls/detail.html',{'question':question})
#get_object_or_404() 函数将模型Question作为它的第一个参数，任意数量的关键字参数作为它的第二个参数，
#它会将这些关键字参数传递给模型管理器中的get() 函数,如果对象不存在，引发一个 Http404异常.

#视图
#def results(request,question_id):                         
#	response="You're looking at the results of question %s."
#	return HttpResponse(response % question_id)

#def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'polls/results.html', {'question': question

#def vote(request,question_id):
#	return HttpResponse("You're voting on question %s." % question_id)

#def vote(request, question_id):
#	p = get_object_or_404(Question, pk=question_id)
#	try:
#		selected_choice = p.choice_set.get(pk=request.POST['choice'])
#	except (KeyError, Choice.DoesNotExist):
#	# Redisplay the question voting form.
#	return render(request, 'polls/detail.html', {
#		'question':p,
#		'error_message': "You didn't select a choice.",
#		})
#else:
#	selected_choice.votes += 1
#	selected_choice.save()
#	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#request.POST 是一个类似字典的对象，让你可以通过关键字的名字获取提交的数据.request.POST的值永远是字符串.
#request.POST['choice'] 以字符串形式返回选择的Choice的ID,如果在POST数据中没有提供choice，request.POST['choice']将引发一个KeyError.
#try...except代码检查KeyError，如果没有给出choice将重新显示Question表单和一个错误信息。
#增加Choice的得票数之后，返回一个 HttpResponseRedirect而不是常用的HttpResponse。HttpResponseRedirect只接收一个参数：用户将要被重定向的URL.
#成功处理POST数据后总是返回一个HttpResponseRedirect.
#reverse()函数避免了在视图函数中硬编码URL,它需要我们给出我们想要跳转的视图的名字和该视图所对应的URL模式中需要给该视图提供的参数.
#reverse() 调用将返回一个这样的字符串:'/polls/5/results/',5是p.id的值,重定向的URL将调用'results'视图来显示最终的页面.
#request是一个HttpRequest对象.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """返回最后5个发布的问题."""
        return Question.objects.filter(
           pub_date__lte=timezone.now()
     ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
         return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
	p=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=p.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
			'question':p,
			'error_message':"You didn't select a choice.",
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))