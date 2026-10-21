from django.test import SimpleTestCase
from django.urls import reverse


class PageTests(SimpleTestCase):
    def test_pages_render(self):
        for name, title in [
            ("projects:index", "Projects"),
            ("blog:index", "Blog"),
            ("contact:index", "Contact"),
        ]:
            with self.subTest(name=name):
                response = self.client.get(reverse(name))
                self.assertContains(response, f"<h1>{title}</h1>")
