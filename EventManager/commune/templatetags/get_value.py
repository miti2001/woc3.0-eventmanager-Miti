from django import template

register = template.Library()

@register.filter
def get_value(row):
    return row.items()