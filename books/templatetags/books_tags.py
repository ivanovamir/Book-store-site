from django import template
from books.models import *

register = template.Library()

@register.simple_tag(name='get_categories')
def get_categories():
    return Category.objects.all()