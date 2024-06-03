from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=255, null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    at_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["is_done", "-at_created"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
