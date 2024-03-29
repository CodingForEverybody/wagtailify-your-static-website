from django import template
from wagtail.models import Page

register = template.Library()

@register.simple_tag
def get_navbar_pages():
    return Page.objects.live().public().in_menu().filter(depth__gt=2)
