# -*- coding:utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)    #问题属性
	pub_date=models.DateTimeField('date published')   #发布时间属性
	def __unicode__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question=models.ForeignKey(Question)
	choice_text=models.CharField(max_length=200)      #选择的内容
	votes=models.IntegerField(default=0)                #选择的得票统计
	def __unicode__(self):
		return self.choice_text	


#有了这些代码，Django就能够自动完成以下两个功能：
#为该应用创建数据库表（CREATE TABLE 语句）。
#为Question对象和Choice对象创建一个访问数据库的python API。

#每个模型都用一个类表示，该类继承自django.db.models.Model.
#每个字段通过Field类的一个实例表示--字符字段CharField,日期字段DateTimeField,整形字段IntegerField.这种方法告诉Django，每个字段中保存着什么类型的数据
#我们使用ForeignKey定义了一个关联.它告诉Django每个Choice都只关联一个Question。

'''
API
>>> from polls.models import Question, Choice

# Make sure our __str__() addition worked.
>>> Question.objects.all()
[<Question: What's up?>]

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
[<Question: What's up?>]
>>> Question.objects.filter(question_text__startswith='What')
[<Question: What's up?>]

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
[]

# Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
'''