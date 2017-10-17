from django.conf.urls import url
from simplemooc.core import views as viewsCore

urlpatterns = [
	url(r'^$', viewsCore.home, name='home'),
	url(r'^contato/$', viewsCore.contact, name='contact'),
]