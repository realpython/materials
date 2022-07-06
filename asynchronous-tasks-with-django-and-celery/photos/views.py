from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect

from photos.models import Photo
from photos.tasks import fetch_latest_flickr_image


class PhotoView(ListView):
    model = Photo

    def post(self, request):
        num_images = int(request.POST["number_of_images_to_fetch"])
        for _ in range(num_images):
            task = fetch_latest_flickr_image.delay()
            if task.successful():  # Isn't successfull right after being called, so doesn't work
                return redirect("photos:photoview")
            else:
                print(f"{task.id} 🥵🥵🥵🥵🥵🥵🥵🥵🥵🥵")

        messages.add_message(
            self.request,
            messages.INFO,
            f"""Fetching {num_images} photos in the background...
                            Reload when ready!""",
        )
        return redirect("photos:photoview")