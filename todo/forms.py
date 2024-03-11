from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local"
            }
        )
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tag",)
