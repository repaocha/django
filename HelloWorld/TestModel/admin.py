# -*- coding:utf-8 -*-


from django.contrib import admin
from TestModel.models import Test,Contact,Tag
 
# Register your models here.
class TagInline(admin.TabularInline):
     model=Tag

class ContactAdmin(admin.ModelAdmin):
    inlines=[TagInline]   #Inline内联
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
#实现将Test,Tag,Contact模块添加到后台管理


#为什么用admin.site.register(x)注册了x模块，后台却无法显示？
#admin后台管理模块，第一步是执行autodiscover函数，该函数是根据settings.INSTALLED_APPS来逐个处理每个模块的，
#注册了模块却无法生效，肯定是因为没有将模块添加到配置文件的INSTALLED_APPS(setting.py)中。