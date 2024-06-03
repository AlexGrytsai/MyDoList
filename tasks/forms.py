from django.contrib.auth.forms import UserCreationForm
from django import forms

from tasks.models import User, Task, Tag


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
        required=False
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "deadline",
            "tags",
        )
