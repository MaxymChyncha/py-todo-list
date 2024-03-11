from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=64)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tag = models.ManyToManyField(
        to=Tag,
        related_name="tasks"
    )

    class Meta:
        ordering = ("status", "-datetime",)

    def __str__(self) -> str:
        return f"{self.content}. Status {self.status}"
