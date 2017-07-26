# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Choice,Question

# Register your models here.

#admin.site.register(Question)    #构造一个默认的表单表示

#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']
#admin.site.register(Question, QuestionAdmin)   #自定义管理界面中表单的外观和功能

class ChoiceInline(admin.TabularInline):        #StackedInline:显示所有关联的Choice 对象的字段占用大量的屏幕空间.
     model=Choice                                       #TabularInline:以表格的形式显示内嵌的相关联对象的方法
     extra=3

class QuestionAdmin(admin.ModelAdmin):           #把表单分割成字段集
     fieldsets=[
          (None,                 {'fields':['question_text']}),
          ('Data information',{'fields':['pub_date'],'classes':['collapse']}),
     ]
     inlines=[ChoiceInline]                  #添加关联对象
     list_display=('question_text','pub_date')   #一个要显示的字段名称的元组，在对象的变更列表页面上作为列显示
admin.site.register(Question,QuestionAdmin)
