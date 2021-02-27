from django import template

register =template.Library()

@register.filter(name='cut')
def cut(value,arg):
    '''
    saca todos los valores "arg" del string
    '''
    return value.replace(arg,'')

#register.filter('cut',cut)

