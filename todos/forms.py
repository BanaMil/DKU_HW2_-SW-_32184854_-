from django import forms
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['lecture_name', 'description', 'due_date', 'completed']
