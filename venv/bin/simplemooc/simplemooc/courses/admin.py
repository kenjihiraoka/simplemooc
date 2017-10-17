from django.contrib import admin
from .models import Course

# Register your models here.

#abre abas de para visualizar os dados no list_display e abre um campo de pesquisa como no search_fields
class CourseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

#login padrão do django, apenas essa linha ja faz tudo do login e chama o CourseAdmin
admin.site.register(Course, CourseAdmin)