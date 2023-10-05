from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect


from .models import Task, Tag


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "tags", "done"]
    success_url = reverse_lazy("todo_app:task-list")


class TaskListView(ListView):
    model = Task
    paginate_by = 4


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", "deadline", "tags", "done"]
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:task-list")


def task_done_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo_app:task-list"))


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo_app:tags-list")


class TagListView(ListView):
    model = Tag
    paginate_by = 4


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo_app:tags-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tags-list")