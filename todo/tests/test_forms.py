from django.test import TestCase

from todo.forms import TaskForm
from todo.models import Tag


class TaskFormTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="Mate"
        )
        self.form_data = {
            "content": "Do something",
            "deadline": "2024-03-11T12:00:00Z",
            "tag": [1],
        }

    def test_valid_form(self):
        form = TaskForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        self.form_data["content"] = ""
        form = TaskForm(data=self.form_data)
        self.assertFalse(form.is_valid())
