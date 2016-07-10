from django.conf.urls import url, include
from django.template import RequestContext, loader

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<comment_id>[0-9]+)/addchildcomment/$', views.addchildcomment, name='addchildcomment'),
    url(r'^addcomment/$', views.addcomment, name='addcomment'),
    url(r'^startproject/$', views.startproject, name='startproject'),
    url(r'^chess/$', views.chess, name='chess'),
    url(r'^csair/$', views.csair, name='csair'),
    url(r'^webportfolio/$', views.webportfolio, name='webportfolio'),
    url(r'^show_login/$', views.show_login, name='show_login'),
    url(r'^show_register/$', views.show_register, name='show_register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]