from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def nav(context, view_name, label):
    url = reverse(view_name)
    resolver_match = context.request.resolver_match
    if_active = 'active' if resolver_match.url_name == view_name else ''
    return mark_safe("""
        <li class="nav-item %(if_active)s">
            <a class="nav-link" href="%(url)s" id="%(view_name)s">%(label)s</a>
        </li>
    """ % {'if_active': if_active, 'url': url, 'view_name': view_name, 'label': label})
