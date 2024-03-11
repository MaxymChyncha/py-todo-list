from django.test import TestCase
from django.urls import reverse

from todo.models import Task

TASK_PK = 1
TASK_LIST_URL = reverse("todo:index")
TASK_CHANGE_STATUS_URL = reverse("todo:change-status", kwargs={"pk": TASK_PK})


class TaskViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Do something",
            datetime="2024-03-10T07:00:00Z",
            deadline="2024-03-09T10:00:00Z",
            status=False,
        )

    def test_task_retrieve(self):
        res = self.client.get(TASK_LIST_URL)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["task_list"]),
            list(Task.objects.all())
        )
        self.assertTemplateUsed(res, "todo/index.html")

    def test_change_task_status(self):
        res = self.client.get(TASK_CHANGE_STATUS_URL)
        self.task.refresh_from_db()

        self.assertEqual(res.status_code, 302)
        self.assertTrue(self.task.status)

        res = self.client.get(TASK_CHANGE_STATUS_URL)
        self.task.refresh_from_db()

        self.assertEqual(res.status_code, 302)
        self.assertFalse(self.task.status)
