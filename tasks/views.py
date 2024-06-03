from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from tasks.forms import UserRegistrationForm, TaskCreateForm
from tasks.models import Task, User, Tag


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration/register_form.html"

    success_url = reverse_lazy("tasks:login")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskCreateForm

    success_url = reverse_lazy("tasks:my-tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referer"] = self.request.META.get("HTTP_REFERER")
        context["is_update"] = False

        return context


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskCreateForm

    success_url = reverse_lazy("tasks:task-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referer"] = self.request.META.get("HTTP_REFERER")
        context["is_update"] = True

        return context


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referer"] = self.request.META.get("HTTP_REFERER")

        return context


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    template_name = "tasks/tag_form.html"
    fields = ("name",)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TagCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referer"] = self.request.META.get("HTTP_REFERER")

        return context

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse_lazy("tasks:my-tasks")


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = "tasks/tag_form.html"
    fields = ("name",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referer"] = self.request.META.get("HTTP_REFERER")

        return context

    def get_success_url(self):
        next_url = self.request.GET.get("next")
        if next_url:
            return next_url
        return reverse_lazy("tasks:tag-list")


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["referer"] = self.request.META.get("HTTP_REFERER")

        return context


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = "tasks/tag_list.html"

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)
