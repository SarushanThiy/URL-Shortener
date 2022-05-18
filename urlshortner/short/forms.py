from django import forms
from .models import Http

class NewForm(forms.ModelForm):
    original = forms.URLField()

    class Meta:
        model = Http
        fields = ['original']
