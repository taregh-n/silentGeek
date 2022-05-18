from django import template

register = template.Library()


@register.filter('is_active')
def is_active(obj):
    return obj.filter(active = True)