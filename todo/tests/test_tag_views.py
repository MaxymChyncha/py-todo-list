from django.test import TestCase
from django.urls import reverse

from todo.models import Tag

TAG_LIST_URL = reverse("todo:tag-list")


class TagViewTest(TestCase):

    def test_tag_retrieve(self):
        Tag.objects.create(name="Mate")
        res = self.client.get(TAG_LIST_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["tag_list"]),
            list(Tag.objects.all())
        )
        self.assertTemplateUsed(res, "todo/tag_list.html")
