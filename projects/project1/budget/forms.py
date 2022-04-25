from django import forms
from budget.models import BudgetItem, BudgetCategory

class BudgetForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    category = forms.ModelChoiceField(queryset=BudgetCategory.objects.all())
    projected = forms.IntegerField()
    actual = forms.IntegerField()

    class Meta():
        model = BudgetItem
        fields = ('description', 'category', 'projected', 'actual')
