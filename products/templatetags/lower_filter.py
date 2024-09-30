from django import template

register = template.Library()

@register.filter()
def make_lower(value):
	return value.lower()
