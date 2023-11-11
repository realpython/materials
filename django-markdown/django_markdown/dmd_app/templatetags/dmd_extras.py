import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from dmd_app.markdown_extensions import SlugFieldExtension

register = template.Library()


@register.filter
@stringfilter
def render_markdown(value):
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite", SlugFieldExtension()]
    )
    return mark_safe(md.convert(value))
