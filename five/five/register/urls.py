from django.conf.urls import  url
from register import views

app_name='basic'

urlpatterns=[
	url('index',views.index, name='index'),
	url('register',views.register, name='register'),
	url('log', views.log, name='log'),
	url('lout', views.lout,name='lout')
]