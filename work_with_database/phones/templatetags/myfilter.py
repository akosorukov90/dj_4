from django import template
from django.template.defaultfilters import slugify

register = template.Library()


@register.filter()
def my_slug(name):
    slug = slugify(name)
    return slug
