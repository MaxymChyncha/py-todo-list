from django.test import TestCase

from todo.models import Task, Tag


class TaskModelTest(TestCase):
    def test_task_str(self):
        task = Task.objects.create(
            content="Learn 20 new words",
            datetime="2024-03-10T07:00:00Z",
        )
        self.assertEqual(
            str(task),
            f"{task.content}. Status {task.status}"
        )


class TagModelTest(TestCase):
    def test_task_str(self):
        tag = Tag.objects.create(
            name="Mate"
        )
        self.assertEqual(str(tag), tag.name)
