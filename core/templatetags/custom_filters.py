# core/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return value  # If there's an error, return the original value
