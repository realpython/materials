import json
from urllib.request import urlopen
from urllib.error import URLError

from django.db.utils import IntegrityError

from .models import Photo

from celery import shared_task


FLICKR_JSON_FEED_URL = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1"


@shared_task(
    bind=True, max_retries=None
)  # Keep trying until there are the requested n# images
def fetch_latest_flickr_image(self, *args, **kwargs):
    """Get the latest image from the Flickr public image feed and save it to the database."""

    with urlopen(FLICKR_JSON_FEED_URL) as response:
        body = response.read()

    feed = json.loads(body)
    images = feed["items"]
    flickr_image = images[0]

    # Avoid saving the same image multiple times
    try:
        photo = Photo(
            title=flickr_image["title"],
            link=flickr_image["link"],
            image_url=flickr_image["media"]["m"],
            description=flickr_image["description"],
        )
        photo.save()
    except IntegrityError as e:
        # The unique link is already in the database
        print(f"No new public image yet: {e}")
        raise self.retry(countdown=10)
    except URLError as e:
        print(f"Couldn't fetch image feed: {e}")
        raise self.retry(countdown=10)

    return flickr_image["title"][:20]
