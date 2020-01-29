from django import template


register = template.Library()

@register.filter(name='get_by_index')
def get_by_index(value, index):
    """索引取值"""
    return value[index] if index in value else None