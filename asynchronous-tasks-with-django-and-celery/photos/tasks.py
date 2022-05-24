import json
from urllib.request import urlopen

from .models import Photo

from celery import shared_task


FLICKR_JSON_FEED_URL = "https://api.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1"


@shared_task(bind=True, max_retries=None)  # Keep trying until there are the requested n# images
def fetch_latest_flickr_image(self, *args, **kwargs):
    """Gets the latest image from the Flickr public image feed and saves it to the database."""

    with urlopen(FLICKR_JSON_FEED_URL) as response:
        body = response.read()
    
    feed = json.loads(body)
    images = feed['items']
    flickr_image = images[0]
    # Assure you avoid saving the same image multiple times
    if not Photo.objects.filter(link=flickr_image['link']).exists():
        photo = Photo(
            title=flickr_image['title'],
            link=flickr_image['link'],
            image_url=flickr_image['media']['m'],
            description=flickr_image['description']
        )
        photo.save()
    else:
        print("No new public image yet.")
        raise self.retry(countdown=10)
    return flickr_image["title"][:20]
