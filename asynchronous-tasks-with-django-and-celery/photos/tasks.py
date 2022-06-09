import json
from urllib.request import urlopen
from urllib.error import URLError

from django.db.utils import IntegrityError

from .models import Photo

from celery import shared_task


FLICKR_FEED_URL = (
    "https://api.flickr.com/services/feeds/photos_public.gne"
    "?format=json"
    "&nojsoncallback=1"
)


@shared_task(bind=True, max_retries=None)
def fetch_latest_flickr_image(self, *args, **kwargs):
    """Fetch image and save it to the database.

    The function pulls the latest image from the Flickr public image feed.
    It always only takes the latest image.
    If the image isn't recorded in the local database, it saves it.
    If something goes wrong, the function tries again
    until the requested number of images have been added to the database.
    """

    try:
        with urlopen(FLICKR_FEED_URL) as response:
            body = response.read()
    except URLError as e:
        print(f"Couldn't fetch image feed: {e}")
        raise self.retry(countdown=10)

    feed = json.loads(body)
    images = feed["items"]
    flickr_image = images[0]

    photo = Photo(
        title=flickr_image["title"],
        link=flickr_image["link"],
        image_url=flickr_image["media"]["m"],
        description=flickr_image["description"],
    )
    try:  # Avoid saving the same image multiple times
        photo.save()
    except IntegrityError as e:
        # The unique link is already in the database
        print(f"No new public image yet: {e}")
        raise self.retry(countdown=10)

    return flickr_image["title"][:20]
