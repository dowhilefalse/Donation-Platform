from collections.abc import Hashable

from django import template


register = template.Library()

@register.filter(name='get_by_index')
def get_by_index(value, index):
    """索引取值"""
    if hasattr(value, '__getitem__'):
        if isinstance(value, Hashable):
            return value[index] if 0 <= index < len(value) else None
        return value[index] if index in value else None