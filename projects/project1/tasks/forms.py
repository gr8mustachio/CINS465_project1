from django import forms
from tasks.models import Task, TaskCategory

CATEGORIES = [ (1, "Home"), (2, "Work"), (3, "School"),
(4, "Personal Improvment"), (5, "Relationships"), (6, "Other") ]

class TaskEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())
    is_completed = forms.BooleanField(required=False)

    class Meta():
        model = Task
        fields = ('description', 'category', 'is_completed')

# class TaskCategoryForm(forms.ModelForm):
#     category = forms.CharField(max_length = 128)
#     CATEGORIES.append((len(CATEGORIES), category))
