import json
from urllib.error import URLError
from urllib.request import urlopen

from celery import Task, shared_task
from django.db.utils import IntegrityError
from django.shortcuts import redirect  # Needs to be returned (?), doesn't work
from django.http import HttpResponse

from .models import Photo
# from .views import PhotoView  # Creates a circular import, doesn't work


class FlickrFeedTask(Task):
    autoretry_for = (URLError, IntegrityError)  # Retry if feed couldn't be reached or if image is already in DB
    max_retries = None  # Keep trying forever
    retry_backoff = True
    retry_backoff_max = 350  # 5 minutes
    retry_jitter = True  # default: https://docs.celeryq.dev/en/stable/userguide/tasks.html#Task.retry_jitter

    FLICKR_FEED_URL = (
        "https://api.flickr.com/services/feeds/photos_public.gne"
        "?format=json"
        "&nojsoncallback=1"
    )        #"&tags=nature"  # avoid NSFW but sacrifice speed?

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print("⏮ Image exists, retrying...")
        return HttpResponse("<h1>Hello? Retry</h1>")
        # redirect("https://www.google.com")
        # PhotoView.as_view()


# Return value of these functions is ignored (https://docs.celeryq.dev/en/latest/reference/celery.app.task.html#celery.app.task.Task.on_success)
# But how do I initiate a WSGI action aside from returning a HttpResponse object in Django?
# I can do other tasks in `on_success` and they run as expected, but for a HTTP request sent from within Django
# IDK how to do that without returning in a function, or calling `.as_view()` on a CBV

    def on_success(self, retval, task_id, args, kwargs):
        return "🎉 Success!!!"
        return print("🎉 Success!!!")
        return HttpResponse("<h1>🎉 Success!!!</h1>")
        # redirect("photos:photoview")
        # PhotoView.as_view()


# TODO: think about splitting up the task into two with distinct aims:
# 1) fetch image
# 2) save image
# However, this makes the retry harder, because 1) would succeed even if 2)
# fails, but retrying 2) when it fails isn't enough. 1) needs to retry until
# both succeed, which makes using a chain() harder or at least IDK how to rn


@shared_task(base=FlickrFeedTask, bind=True)
def fetch_latest_flickr_image(self, *args, **kwargs):
    """Fetch image and save it to the database.

    The function pulls the latest image from the Flickr public image feed.
    It always only takes the latest image.
    If the image isn't recorded in the local database, it saves it.
    If something goes wrong, the function tries again
    until the requested number of images have been added to the database.
    """
    with urlopen(self.FLICKR_FEED_URL) as response:
        body = response.read()

    feed = json.loads(body)
    images = feed["items"]
    flickr_image = images[0]

    photo = Photo(
        title=flickr_image["title"],
        link=flickr_image["link"],
        image_url=flickr_image["media"]["m"],
        description=flickr_image["description"],
    )

    # Fails if the unique link is already in the database
    photo.save()

    return flickr_image["title"][:20]
