from django import forms
from .models import Test

from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Test nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Test tavsifi'}),
        }