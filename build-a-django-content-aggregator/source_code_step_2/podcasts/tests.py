from django.test import TestCase
from django.utils import timezone

from .models import Episode


class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title="My Awesome Podcast Episode",
            description="Look mom, I made it!",
            pub_date=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
            podcast_name="My Python Podcast",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Look mom, I made it!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"
        )

    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "My Python Podcast: My Awesome Podcast Episode"
        )
