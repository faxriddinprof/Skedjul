from django import forms
from .models import DailyExpense

class DailyExpenseForm(forms.ModelForm):
    class Meta:
        model = DailyExpense
        fields = ['date', 'ovqat', 'transport', 'salomatlik', 'boshqa', 'izoh']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ovqat': forms.NumberInput(attrs={'class': 'form-control'}),
            'transport': forms.NumberInput(attrs={'class': 'form-control'}),
            'salomatlik': forms.NumberInput(attrs={'class': 'form-control'}),
            'boshqa': forms.NumberInput(attrs={'class': 'form-control'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
