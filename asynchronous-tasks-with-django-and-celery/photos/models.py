from django.db import models


class Photo(models.Model):
    created_on = models.DateTimeField("Created on", auto_now_add=True)
    updated_on = models.DateTimeField("Updated on", auto_now=True)
    title = models.CharField("Title", max_length=255)
    link = models.URLField(
        "Photo Link", max_length=255, help_text="The URL to the image page")
    image_url = models.URLField(
        "Image URL", max_length=255, help_text="The URL to the image file itself")
    description = models.TextField("Description")

    class Meta:
        ordering = ['-created_on', 'title']

    def __str__(self):
        return self.title[:50]
