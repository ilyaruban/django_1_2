from django import template

register = template.Library()

@register.simple_tag()
def multiply(a,b):
    mult = a*b
    return mult