import time
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView

from photos.tasks import fetch_latest_flickr_image
from photos.models import Photo


class PhotoView(ListView):
    model = Photo
    #template_name = 'photos/photo_list.html'  # Default!
    # paginate_by = 10  # Maybe implement pagination?

    def post(self, *args, **kwargs):
        print(self.request.POST)
        # TODO: refactor to Form in forms.py to allow for validation
        num_images = int(self.request.POST.get("images", 0))
        if num_images:
            for n in range(num_images):
                fetch_latest_flickr_image.delay()

            messages.add_message(self.request,
                                messages.INFO,
                                """Fetching photos in the background...
                                Reload when ready!""")
        return redirect("photos:photoview")
