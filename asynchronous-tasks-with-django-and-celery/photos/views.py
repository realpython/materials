from django.contrib import messages
from django.views.generic import ListView, FormView

from photos.tasks import fetch_latest_flickr_image
from photos.models import Photo
from photos.forms import PhotoFetchForm


class PhotoView(ListView, FormView):
    model = Photo
    form_class = PhotoFetchForm
    success_url = "/"

    def form_valid(self, form):
        num_images = form.cleaned_data["number_of_images_to_fetch"]
        for _ in range(num_images):
            fetch_latest_flickr_image.delay()

        messages.add_message(
            self.request,
            messages.INFO,
            """Fetching photos in the background...
                            Reload when ready!""",
        )
        return super().form_valid(form)
