from django.shortcuts import render
from django.views import generic

from todo.models import Task


class IndexView(generic.ListView):
    model = Task
    paginate_by = 5
    template_name = "todo/index.html"
