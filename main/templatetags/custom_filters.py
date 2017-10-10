from django import template
import humanize

register = template.Library()


@register.filter
def humanize_delta(value):
    return humanize.naturaldelta(value)
