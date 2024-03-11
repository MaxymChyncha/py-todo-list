from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "todo/index.html"

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related("tag")
        return queryset


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self) -> str:
        return reverse("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self) -> str:
        return reverse("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task

    def get_success_url(self) -> str:
        return reverse("todo:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)

    def get_success_url(self) -> str:
        return reverse("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)

    def get_success_url(self) -> str:
        return reverse("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag

    def get_success_url(self) -> str:
        return reverse("todo:tag-list")


def change_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))
