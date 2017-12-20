from django.db import models
from django.conf import settings

# Create your models here.

#Gerencia as pesquisa no banco de dados, com os paramentros abaixo
class CourseManager(models.Manager):
	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | 
			models.Q(description__icontains=query)
		)	

#nossa classe representa uma tabela no banco de dados
class Course(models.Model):
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	description = models.TextField('Descrição Simple', blank=True)
	about = models.TextField('Sobre o Curso', blank=True)
	start_date = models.DateField('Data de Ínicio', null=True, blank=True)
	image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Criado em', auto_now=True)
	objects = CourseManager()

	#printa o nome dos cursos na tabela de admin do login, sem ele aparece Object
	def __str__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return('courses:details', (), {'slug': self.slug})

	class Meta:
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'	
		ordering = ['name']

class Enrollment(models.Model):
	STATUS_CHOICES = (
			(0, 'Pendente'),
			(1, 'Aprovado'),
			(2, 'Cancelado'),
		)

	user = models.ForeignKey(
			settings.AUTH_USER_MODEL, verbose_name='Usuário',
			related_name='enrollments'
		)	
	course = models.ForeignKey(
			Course, verbose_name='Curso', 
			related_name='enrollments'
		)
	status = models.IntegerField(
			'Situação', choices=STATUS_CHOICES, default=0,
			blank=True
		)

	#sempre é importante colocar esse tipo de variavel
	created_at = models.DateTimeField('Criado em', auto_now_add=True)
	updated_at = models.DateTimeField('Atualizado em', auto_now=True)

	def active(self):
		self.status = 1
		self.save()

	class Meta:
		verbose_name='Inscrição'
		verbose_name_plural='Incrições'
		#unique_together permite que o usuário se cadastre apenas uma vez
		#em um curso enquanto ele já estiver inscrito nele, ou seja,
		#é uma relação de 1:1
		unique_together=(('user', 'course'))
