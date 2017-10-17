from django.conf.urls import include, url
from django.contrib.auth import views as authView
from simplemooc.accounts import views as accountView

urlpatterns = [
	url(r'^$', accountView.dashboard, name='dashboard'),

	url(r'^entrar/$', authView.login,
		{'template_name': 'accounts/login.html'}, name='login'),

	url(r'^sair/$', authView.logout,
		{'next_page': 'core:home'}, name='logout'),

	url(r'^cadastro/$', accountView.register, name='register'),

	url(r'^nova-senha/$', accountView.password_reset, name='password_reset'),

	url(r'^confirmar-nova-senha/(?P<key>\w+)/$', accountView.password_reset_confirm, name='password_reset_confirm'),

	url(r'^editar/$', accountView.edit, name='edit'),

	url(r'^editar_senha/$', accountView.edit_password, name='edit_password'),

]