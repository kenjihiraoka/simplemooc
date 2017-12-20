from django.template import Library

register = Library()

from simplemooc.courses.models import Enrollment

@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_course(user):
	enrollments = Enrollment.objects.filter(user=user)
	context = {'enrollments': enrollments}
	return context