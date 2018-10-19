from django.urls import path
from django.conf.urls import url

from .views import homePageView
from . import views

urlpatterns = [
    #path('', homePageView, name='home'),
    #url(r'^$', views.index),
    url(r'^$', views.simple_upload)

]
