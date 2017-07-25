from django.conf.urls import url
from . import view
from . import view,testdb,search
from django.contrib import admin
 
urlpatterns = [
    url(r'^hello$',view.hello),
    url(r'^search-form$',search.search_form),
    url(r'^search$',search.search),
    url(r'^testdb$',testdb.testdb),
    url(r'^admin/', admin.site.urls),
]