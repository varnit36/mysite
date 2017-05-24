from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^now/$', views.current_projects, name='current_projects'),
    url(r'^now/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),

]