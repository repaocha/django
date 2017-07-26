# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.
class Question(models.Model):
	question_text=models.CharField(max_length=200)    #问题属性
	pub_date=models.DateTimeField('date published')   #发布时间属性

	def __unicode__(self):
		return self.question_text


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

