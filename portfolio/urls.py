from django.conf.urls import url
from django.template import RequestContext, loader

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^startproject/$', views.startproject, name='startproject'),
    url(r'^chess/$', views.chess, name='chess'),
    url(r'^csair/$', views.csair, name='csair'),
    url(r'^webportfolio/$', views.webportfolio, name='webportfolio'),
]