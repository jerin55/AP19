from django import template

from network.models import *




register = template.Library()



@register.filter
def delprice(value):

    value1 = value *25/100

    value2 = value+value1

    
    return value2


@register.filter
def counts(value):

    posts = Post.objects.filter(intr_id=value)
    
    return len(posts)