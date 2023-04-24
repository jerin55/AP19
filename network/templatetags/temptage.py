from django import template
from requests import request

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

@register.filter
def counts2(value,value2):

    posts = Post.objects.filter(intr_id=value,creater=value2)
    
    return len(posts)