from django import forms
from django.forms import ModelForm

from .models import Post


class DateInput(forms.DateInput):
    input_type = 'date'

class PromiseForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text','date']
        widgets = {
            'date': DateInput(),
        }