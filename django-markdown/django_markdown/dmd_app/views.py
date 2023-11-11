from django.shortcuts import get_object_or_404, render

from .models import MarkdownContent


def markdown_content_view(request, slug):
    markdown_content = get_object_or_404(MarkdownContent, slug=slug)
    context = {"markdown_content": markdown_content}
    return render(request, "dmd_app/markdown_content.html", context=context)
