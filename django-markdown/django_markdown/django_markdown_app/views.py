from django.shortcuts import render, get_object_or_404
from .models import MarkdownContent


def markdown_content_view(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {"markdown_content": markdown_content}
    return render(
        request, "django_markdown_app/markdown_content.html", context=context
    )
