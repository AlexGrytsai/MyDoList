from django.urls import path

from tasks.views import UserRegistrationView, TaskListView, TaskCreateView, \
    TaskDeleteView, TaskUpdateView, TagCreateView, TagListView, TagDeleteView, \
    TagUpdateView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register-user"),
    path("", TaskListView.as_view(), name="my-tasks"),
    path("add-task/", TaskCreateView.as_view(), name="add-task"),
    path(
        "delete-task/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"
    ),
    path(
        "update-task/<int:pk>/", TaskUpdateView.as_view(), name="update-task"
    ),
    path("add-tag", TagCreateView.as_view(), name="add-tag"),
    path("tag-list/", TagListView.as_view(), name="tag-list"),
    path("delete-tag/<int:pk>/", TagDeleteView.as_view(), name="delete-tag"),
    path("update-tag/<int:pk>/", TagUpdateView.as_view(), name="update-tag"),
]

app_name = "tasks"
