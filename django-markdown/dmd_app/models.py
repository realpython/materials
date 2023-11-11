from django.db import models


class MarkdownContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = "Markdown content"

    def __str__(self):
        return self.title
