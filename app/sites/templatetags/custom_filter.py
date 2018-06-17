from django import template
from django.db.models import Sum, Avg
from django.urls import reverse

register = template.Library()

@register.filter(takes_context=True)
def getSum(value, coloum):
    data = value.aggregate(value = Sum(coloum))
    if data['value'] == None :
        return 0
    else:
        return data['value']
@register.filter(takes_context=True)
def getAverage(value, coloum):
    data = value.aggregate(value = Avg(coloum))
    if data['value'] == None :
        return 0
    else:
        return data['value']


@register.simple_tag
def is_active(request, name, by_path=False):

    if by_path:
        path = reverse(name, kwargs={'pk': by_path})
    else:
        path = reverse(name)
    if request.path == path:
        return ' active '

    return ''