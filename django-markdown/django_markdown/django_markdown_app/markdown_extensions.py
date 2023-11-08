import markdown
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE
from django.urls import reverse


class SlugFieldLinkInlineProcessor(LinkInlineProcessor):
    def getLink(self, data, index):
        href, title, index, handled = super().getLink(data, index)
        if href.startswith("slug"):
            slug = href.split(":")[1]
            relative_url = reverse("markdown-content", args=[slug])
            href = relative_url
        return href, title, index, handled


class SlugFieldExtension(markdown.Extension):
    def extendMarkdown(self, md, *args, **kwargs):
        md.inlinePatterns.register(
            SlugFieldLinkInlineProcessor(LINK_RE, md), "link", 160
        )
