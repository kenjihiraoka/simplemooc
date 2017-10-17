from django.conf.urls import url, include
from simplemooc.courses import views as viewsCourse

urlpatterns = [
	url(r'^$', viewsCourse.index, name='index'),
	#url(r'^(?P<pk>\d+)/$', viewsCourse.details, name='details')
	url(r'^(?P<slug>[\w_-]+)/$', viewsCourse.details, name='details')

]	